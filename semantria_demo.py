import semantria
import uuid
import time

print "Semantria service demo...", "\r\n"

# the consumer key and secret
consumerKey = "c18c1d22-e189-4a92-b34d-dc1155964446"
consumerSecret = "e7faedd6-70c2-487f-a43a-ad89aebf04e9"
initialTexts = [
    "Initial text for processing.", 
    "Initial text for processing.", 
    "Initial text for processing."
    ]

def onRequest(sender, result):
    print "\n", "REQUEST: ", result

def onResponse(sender, result):
    print "\n", "RESPONSE: ", result

def onError(sender, result):
    print "\n", "ERROR: ", result

def onDocsAutoResponse(sender, result):
    print "\n", "AUTORESPONSE: ", len(result), result

def onCollsAutoResponse(sender, result):
    print "\n", "AUTORESPONSE: ", len(result), result

# Creates JSON serializer instance
serializer = semantria.JsonSerializer()

# Initializes new session with the serializer object and the keys.
session	= semantria.Session(consumerKey, consumerSecret, serializer)

# Initialize session callback handlers
# session.Request += onRequest
# session.Response += onResponse
session.Error += onError
#session.DocsAutoResponse +=	onDocsAutoResponse
#session.CollsAutoResponse +=	onCollsAutoResponse

for text in initialTexts:
    # Creates a sample document which need to be processed on Semantria
    # Unique document ID
    # Source text which need to be processed
    doc = { "id":str(uuid.uuid1()).replace("-", ""), "text":text}
    # Queues document for processing on Semantria service
    status = session.queueDocument(doc)
    # Check status from Semantria service
    if status == 202:
        print "Document ", doc["id"], " queued successfully.", "\r\n"

#Count of the sample documents which need to be	processed on Semantria
length	= len(initialTexts)
results	= []

while (len(results) < length):
    print "Please wait 5 sec for documents...", "\r\n"
#As Semantria isn't real-time solution you need to wait some time before getting of the processed results In real application here can be implemented two separate jobs, one for queuing of source data another one for retreiving
# Wait ten seconds while Semantria process queued document
time.sleep(5)
# Requests processed results from Semantria service
status = session.getProcessedDocuments()
# Check status from Semantria service
if isinstance(status, list):
    for object in status:
        results.append(object)
printlen(status), "	documents	received	successfully.", "\r\n"
for data in results:
    # Printing of document sentiment score
    print "Document ", data["id"], " Sentiment score: ", data["sentiment_score"],"\r\n"
    
    # Printing of document themes
    print "Document	themes:", "\r\n"
    if data["doc_themes"]:
        for theme in data["doc_themes"]:
            print " ", theme["title"], " (sentiment: ",
            theme["sentiment_score"], ")", "\r\n"
    
    # Printing of document entities
    print "Entities:", "\r\n"
    if data["entities"]:
        for entity in data["entities"]:
            print " ", entity["normalized_form"], " : ", entity["entity_type"], " (sentiment: ", entity["sentiment_score"], ")", "\r\n"

i = raw_input("Enter to close app ...")

var places = [{'name': 'Camden'},
 {'name': 'Greenwich'},
 {'name': 'Hackney'},
 {'name': 'Hammersmith and Fulham'},
 {'name': 'Islington'},
 {'name': 'Royal Borough of Kensington and Chelsea'},
 {'name': 'Lambeth'},
 {'name': 'Lewisham'},
 {'name': 'Southwark'},
 {'name': 'Tower Hamlets'},
 {'name': 'Wandsworth'},
 {'name': 'Westminster'},
 {'name': 'Barking and Dagenham'},
 {'name': 'Barnet'},
 {'name': 'Bexley'},
 {'name': 'Brent'},
 {'name': 'Bromley'},
 {'name': 'Croydon'},
 {'name': 'Ealing'},
 {'name': 'Enfield'},
 {'name': 'Haringey'},
 {'name': 'Harrow'},
 {'name': 'Havering'},
 {'name': 'Hillingdon'},
 {'name': 'Hounslow'},
 {'name': 'Kingston upon Thames'},
 {'name': 'Merton'},
 {'name': 'Newham'},
 {'name': 'Redbridge'},
 {'name': 'Richmond upon Thames'},
 {'name': 'Sutton'},
 {'name': 'Waltham Forest'}]

function PlaceListCtrl($scope) {
  $scope.places = places;
  $scope.current_place = null;
  $scope.show_spinner = false;

  $scope.fetchPlace = function(place){
    $.ajax('/search', {
      beforeSend: function(){
        $scope.show_spinner = true;
      },
      complete: function(){
        $scope.show_spinner = false;
        $scope.$apply();
      },
      data: {'place': place},
      dataType: 'json',
      success: function(response){
        $scope.current_place = response;
      }
    });
  }


}
function PlaceListCtrl($scope) {
  $scope.places = [{name: 'Camden'}, {name: 'Grenwich'}, {name: 'Hackney'}];
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
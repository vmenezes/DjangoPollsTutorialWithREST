angular.module('starter.controllers', [])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {
  
  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //$scope.$on('$ionicView.enter', function(e) {
  //});
  
  // Form data for the login modal
  $scope.loginData = {};

  // Create the login modal that we will use later
  $ionicModal.fromTemplateUrl('templates/login.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modal = modal;
  });

  // Triggered in the login modal to close it
  $scope.closeLogin = function() {
    $scope.modal.hide();
  };

  // Open the login modal
  $scope.login = function() {
    $scope.modal.show();
  };

  // Perform the login action when the user submits the login form
  $scope.doLogin = function() {
    console.log('Doing login', $scope.loginData);

    // Simulate a login delay. Remove this and replace with your login
    // code if using a login system
    $timeout(function() {
      $scope.closeLogin();
    }, 1000);
  };
})

.controller('PlaylistsCtrl', function($scope) {
  $scope.playlists = [
    { title: 'Reggae', id: 1 },
    { title: 'Chill', id: 2 },
    { title: 'Dubstep', id: 3 },
    { title: 'Indie', id: 4 },
    { title: 'Rap', id: 5 },
    { title: 'Cowbell', id: 6 }
  ];
})

.controller('PlaylistCtrl', function($scope, $stateParams) {
})

.controller('PollsCtrl', function($scope, $stateParams, $http) {
    var config = {headers: {
            'Authorization': 'Token 3f7ea2dbe3c2cab9b55346200d7ef4796f53c731',
        }
    };
    
    $http.get('http://127.0.0.1:8000/polls/api/questions/', config).
        success(function(data, status){
            $scope.polls = data;
        }).
        error(function(data, status){
            console.log('ERROR LOADING CHOICES LIST')
            console.log(status);
            console.log(data);
        });
})

.controller('PollCtrl', function($scope, $stateParams, $http) {
    var config = {headers: {
            'Authorization': 'Token 3f7ea2dbe3c2cab9b55346200d7ef4796f53c731',
        }
    };
    
    $http.get('http://127.0.0.1:8000/polls/api/choices/?question_id=' + $stateParams.pollId, config).
        success(function(data, status){
//            console.log(data);
//            for (i=0; i < data.length; i++){
//                console.log(data[i].choice_text);
//            }
            $scope.choices = data;
//            $scope.polls = data;
//            $scope.poll = $scope.polls[$stateParams.pollId];
            
        }).
        error(function(data, status){
            console.log('ERROR LOADING CHOICE DETAILS')
            console.log(status);
            console.log(data);
        });
});
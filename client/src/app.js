var app = angular.module('chimeRoom', ['ngRoute']);

app.config(function ($routeProvider) {
    $routeProvider.
        when("/manage",
            {
                templateUrl: "manage/manage.html",
                controller: "ManageController"
            }
        ).
	when("/book",
            {
                templateUrl: "book/book.html",
                controller: "BookController"
            }
        ).otherwise(
        {
            templateUrl: "404.html",
            controller: "404Controller"
        }
        )
    }
)
var chimeroom = {'user_name':'Richa Gupta','user_email':'ric.gupta1103@gmail.com','base_url':'http://greytip.com:8000'}
app.constant('chimeroom',chimeroom)
app.controller('ManageController',['$scope','chimeroom','$http', function ($scope,chimeroom,$http) {
    $scope.itemNumber = 0 ;
    $scope.repeatElement = [];
    $scope.amenitiesTypeList = [{name: 'Wifi', id: 'wifi'}, {name: 'White Board', id: 'whiteboard'},
     {name: 'Projector', id: 'projector'}, {name: 'Internet', id: 'internet'},
     {name: 'Intercom', id: 'intercom'}, {name: 'Tele-conferencing', id: 'teleconferencing'}, {name: 'Video-conferencing', id: 'videoconferencing'}];
    $scope.keywordType = function(){
        $scope.keyword_type_text = {}
        angular.forEach($scope.amenitiesTypeList, function (keyword_type) {
            if (keyword_type.checked) {
                $scope.keyword_type_text[keyword_type.id] = true
            } else {
                $scope.keyword_type_text[keyword_type.id] = false
            }
        })

    }
    $scope.CreateForm = function (formCreateRoom) {
        $scope.form_object = {};
        $scope.form_object["conferenceName"] = formCreateRoom.conferenceName.$modelValue;
        $scope.form_object["numberOfSeats"] = formCreateRoom.numberOfSeats.$modelValue;
        $scope.form_object["ameneties"] = $scope.keyword_type_text;
        $scope.form_object["floorValue"] = $scope.floorValue;
        console.log($scope.floorValue)
        $http({
            method: 'POST',
            url: chimeroom.base_url + '/addroom',
            data: $scope.form_object,
//            headers: {'Content-Type': undefined}
        }).then(
            function (result) {

            },
            function (err) {
                console.log(err)
            });
        };
}]);
app.controller('BookController',['$scope', function ($scope) {
    
}]);

app.controller('404Controller', ['$scope', function ($scope) {
}]);

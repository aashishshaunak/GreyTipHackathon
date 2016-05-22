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
var chimeroom = {'user_name':'Richa Gupta','user_email':'ric.gupta1103@gmail.com','base_url':'http://localhost:8000'}
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
    $scope.viewRooms = function(){
        $http({
                method: 'GET',
                url: chimeroom.base_url + '/viewrooms',
                data: null
        }).then(
            function (result) {
                $scope.availableRooms = result.data
                console.log($scope.availableRooms)

            },
            function (err) {
                console.log(err)
            });
    }
    $scope.viewRooms()
    $scope.deleteProject = function (project_id) {
        $http({
            method: 'DELETE',
            url: chimeroom.base_url + '/viewrooms',
        }).then(
            function (result) {
                alert('Deleted successfully')
            },
            function (err) {
                console.log(err)
            });

        };
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
        }).then(
            function (result) {
                $scope.viewRooms()
            },
            function (err) {
                console.log(err)
            });
    };

    $scope.EditProject = function (project_id) {
        $http({
            method: 'GET',
            url: chimeroom.base_url + '/editroom',
            data: { name: 'gabbar' }
        }).then(
            function (result) {
                console.log(result.data);
                alert('edit successfully')
            },
            function (err) {
                console.log(err)
            });

        };

}]);
app.controller('BookController',['$scope', 'chimeroom', '$http', function ($scope, chimeroom, $http) {
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();
    $scope.minDate = yyyy + '-' + ("0" + mm).slice(-2) + '-' + dd;

    $scope.itemNumber = 0 ;
    $scope.repeatElement = [];
    $scope.amenitiesTypeList = [{name: 'Wifi', id: 'wifi'}, {name: 'White Board', id: 'whiteboard'},
     {name: 'Projector', id: 'projector'}, {name: 'Internet', id: 'internet'},
     {name: 'Intercom', id: 'intercom'}, {name: 'Tele-conferencing', id: 'teleconferencing'},
     {name: 'Video-conferencing', id: 'videoconferencing'}];
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
        $scope.form_object["user_name"] = chimeroom.user_name;
        $scope.form_object["user_email"] = chimeroom.user_email;
        $scope.form_object["numberOfSeats"] = formCreateRoom.numberOfSeats.$modelValue;
        $scope.form_object["ameneties"] = $scope.keyword_type_text;
        $scope.form_object["floorValue"] = $scope.floorValue;
        var meeting_date = $scope.date;
        var meeting_startat = $scope.timein;
        var meeting_endat = $scope.timeout;
        meeting_startat.setDate(meeting_date.getDate())
        meeting_startat.setMonth(meeting_date.getMonth())
        meeting_startat.setYear(meeting_date.getFullYear())
        meeting_endat.setDate(meeting_date.getDate())
        meeting_endat.setMonth(meeting_date.getMonth())
        meeting_endat.setYear(meeting_date.getFullYear())
        $scope.form_object["meeting_start"] = meeting_startat;
        $scope.form_object["meeting_end"] = meeting_endat;
        $http({
            method: 'POST',
            url: chimeroom.base_url + '/bookroom',
            data: $scope.form_object,
        }).then(
            function (result) {

            },
            function (err) {
                console.log(err)
            });
    };

}]);

app.controller('404Controller', ['$scope', function ($scope) {
}]);

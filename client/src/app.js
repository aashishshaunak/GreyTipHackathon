var app = angular.module('chimeRoom', ['ngRoute']);

app.config(function ($routeProvider) {
    $routeProvider.
        when("/manage",
            {
                templateUrl: "manage/manage.html",
                controller: "ManageController"
            }
        ).otherwise(
        {
            templateUrl: "404.html",
            controller: "404Controller"
        }
        )
    }
)

app.controller('ManageController',['$scope', function ($scope) {
}]);

app.controller('404Controller', ['$scope', function ($scope) {
}]);


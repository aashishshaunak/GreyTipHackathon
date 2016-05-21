var app = angular.module('chimeRoom', ['ngRoute']);

app.config(function ($routeProvider) {
    $routeProvider.
        when("/",
            {
                templateUrl: "index.html",
                controller: "mainController"
            }
        ).when("/manage",
            {
                templateUrl: "manage/index.html",
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

app.controller('mainController', ['$scope', function ($scope) {
}]);

app.controller('ManageController',['$scope', function ($scope) {
}]);

app.controller('404Controller', ['$scope', function ($scope) {
}]);


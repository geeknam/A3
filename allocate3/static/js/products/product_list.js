function ProductListController($scope, $http) {
    $http.get('/api/products/').success(function(response){
        $scope.products = response.results;
    });
}

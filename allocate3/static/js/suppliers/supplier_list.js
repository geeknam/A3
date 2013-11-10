function SupplierListController($scope, $http) {
    $http.get('/api/suppliers/').success(function(response){
        $scope.suppliers = response.results;
    });
}

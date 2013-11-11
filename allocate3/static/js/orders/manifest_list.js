function ManifestListController($scope, $http) {
    $http.get('/api/manifests/').success(function(response){
        $scope.manifests = response.results;
    });
}

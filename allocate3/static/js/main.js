$(document).ready(function() {
    $('.filter.menu .item').tab();
    $('.ui.rating').rating({clearable: true});
    $('.ui.sidebar').sidebar('attach events', '.launch.button');
    $('.ui.dropdown').dropdown();
});

var allocate = angular.module('AllocateApp', []);

allocate.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('<[');
    $interpolateProvider.endSymbol(']>');
});


allocate.directive('onKeyupFn', function() {
    return function(scope, elm, attrs) {
        var keyupFn = scope.$eval(attrs.onKeyupFn);
        elm.bind('keyup', function(evt) {
            scope.$apply(function() {
                keyupFn.call(scope, evt);
            });
        });
    };
});


var typewatch = function(){
    var timer = 0;
    return function(callback, ms){
        clearTimeout (timer);
        timer = setTimeout(callback, ms);
    };
}();



function SearchController($scope, $http) {
    var $suggestions = $("#suggestions");
    var $search_box = $("#site-search-box");

    $scope.type = 'invoices';


    $scope.search_callback = function(response) {
        $scope.results = response.results;
        if($scope.results.length > 0) {
            $suggestions.removeClass("hide");
        }
        else{
            $suggestions.addClass("hide");
        }
    };

    $scope.search = function(){
        $scope.type = 'products';
        typewatch(function(){
            return $http.get('/api/' + $scope.type + '/?search=' + $scope.keyword).success($scope.search_callback);
        }, 500);
    };

    $scope.handleKeypress = function(evt){
        evt.preventDefault();
        var $highlighted = $suggestions.find('.highlighted:first');
        console.log(evt.keyCode);
        if(([13, 38, 40]).indexOf(evt.keyCode, true) == -1) return true;
        switch(evt.keyCode){
            case 40:
                if($highlighted.length){
                    var next = $highlighted.removeClass('highlighted').next();
                    next.addClass('highlighted');
                    $search_box.val(next.find('a').text());
                }
                else{
                    var first = $suggestions.find('li:first');
                    first.addClass('highlighted');
                    $search_box.val(first.find('a').text());
                }
                break;
            case 38:
                if($highlighted.length){
                    var prev = $highlighted.removeClass('highlighted').prev();
                    prev.addClass('highlighted');
                    $search_box.val(prev.find('a').text());
                }
                else{
                    var last = $suggestions.find('li:last');
                    last.addClass('highlighted');
                    $search_box.val(last.find('a').text());
                }
                break;
            case 13:
                var last = $suggestions.find('li:last');
                console.log(last.find('a').attr('href'));
                window.location = $search_box.val(last.find('a').attr('href'));
                break;
        }
    };

}

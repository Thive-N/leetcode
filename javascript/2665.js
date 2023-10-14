var createCounter = function (init) {
    n = init;
    function increment() {
        n++;
        return n;
    }
    function decrement() {
        n--;
        return n;
    }
    function reset() {
        n = init;
        return n;
    }

    return {
        increment,
        decrement,
        reset,
    };
};

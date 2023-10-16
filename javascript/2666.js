var once = function (fn) {
    n = 0;
    return function (...args) {
        if (n === 0) {
            n++;
            return fn(...args);
        }
    };
};

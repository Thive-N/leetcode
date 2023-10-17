var cancellable = function (fn, args, t) {
    var timeout = setTimeout(() => fn(...args), t);
    var ct = () => clearTimeout(timeout);
    return ct;
};

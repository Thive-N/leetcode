var cancellable = function (fn, args, t) {
    fn(...args);
    var interval = setInterval(() => fn(...args), t);
    const cf = () => clearInterval(interval);
    return cf;
};

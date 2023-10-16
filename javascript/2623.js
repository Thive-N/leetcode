function memoize(fn) {
    let memo = {};
    return function (...args) {
        const a = args.join(" ");
        const c = memo[a];
        if (c != undefined) {
            return c;
        }
        memo[a] = fn(...args);
        return memo[a];
    };
}

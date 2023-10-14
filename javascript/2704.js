var expect = function (val) {
    function toBe(v2) {
        if (val === v2) return true;
        throw new Error("Not Equal");
    }

    function notToBe(v2) {
        if (val !== v2) return true;
        throw new Error("Equal");
    }
    return {
        toBe,
        notToBe,
    };
};

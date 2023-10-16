function compose(functions) {
    return (x) => functions.reduceRight((total, f) => f(total), x);
}

let zip = (xs, ...rest) => (Array.isArray(xs) ? xs : []).map((e, i) => [e, ...rest.map((ee) => ee[i]? ee[i]:undefined)]);
let zip = (xs, ...rest) => xs.map((e, i) => [e, ...rest.map((ee) => ee[i]? ee[i]:undefined)]);
// let zipLongest = (...tuples) => .map((e, i) => [e, ...rest.map((ee) => ee[i]? ee[i]:undefined)]);

Array.prototype.zip = function(...others){
    return zip(this, ...others);
}


import ohm from 'ohm-js';

const reverseStr = (str) => str.split('').reverse().join('');

const grammarStr = `BracketReverse {
    ForwardString = string (ReversedString string)+  -- recurse
                  | string                           -- base

    ReversedString = "(" ForwardString ")"

    string = lower*
}`;

const grammar = ohm.grammar(grammarStr);
const semantics = grammar.createSemantics();

semantics.addOperation('resolve', {
  ForwardString_recurse(first, revStrs, fwdStrs){
    const resolvedStrs = fwdStrs.resolve()
    const zippedRestStrs = revStrs.resolve().map((e, i) => [e, resolvedStrs[i]]);
    return first.sourceString + zippedRestStrs.map((r) => r[0] + r[1]).join('');
  },
  ForwardString_base(str) {
    return str.sourceString;
  },
  ReversedString(_lParen, revStr, _rParen) {
    return reverseStr(revStr.resolve());
  },
  string(str){
    return str.sourceString;
  }
});

export const processBracketString = (string) => {
  const match = grammar.match(string);
  if (match.succeeded()) return semantics(match).resolve();
  throw new Error(`Could not process brakcet string\n${match.message}`);
}

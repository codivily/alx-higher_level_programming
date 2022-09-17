#!/usr/bin/node

function callMeMoby (x, theFunction) {
  while (x > 0) {
    theFunction();
    x -= 1;
  }
}

exports.callMeMoby = callMeMoby;

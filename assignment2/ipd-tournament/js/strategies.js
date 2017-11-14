'use strict';

if (strategies === undefined) {
  var strategies = {};
}

if (cid === undefined) {
  var cid;
}

// Exchange this for your own cid
cid = 'horken';

// Defect: action 0
// Cooperate: action 1


strategies[cid + '10a'] = function () {
  function chooseAction(me, opponent, t) {
  if (t <= 1) {
      return 0;
    }

    else if (opponent[t-2] == 0 && opponent[t-1] == 0 && me[t-1] == 0) {
      return 1;
    }
    
    else if (opponent[t-2] == 0 && opponent[t-1] == 0 && me[t-1] == 1) {
      return 0;
    }

    else if (opponent[t-2] == 0 && opponent[t-1] == 1 && me[t-1] == 0) {
      return 1;
    }

    else if (opponent[t-2] == 0 && opponent[t-1] == 1 && me[t-1] == 1) {
      return 0;
    }

    else if (opponent[t-2] == 1 && opponent[t-1] == 0 && me[t-1] == 0) {
      return 1;
    }
    
    else if (opponent[t-2] == 1 && opponent[t-1] == 0 && me[t-1] == 1) {
      return 0;
    }
    
    else if (opponent[t-2] == 1 && opponent[t-1] == 1 && me[t-1] == 0) {
      return 0;
    }
    
    else if (opponent[t-2] == 1 && opponent[t-1] == 1 && me[t-1] == 1) {
      return 0;
    }

    return 0; // otherwise cooperate
  }

  return chooseAction;
}


strategies[cid + '10b'] = function () {
  function chooseAction(me, opponent, t) {
    if (t <= 1) {
      return 0;
    }

    else if (opponent[t-2] == 0 && opponent[t-1] == 0 && me[t-1] == 0 && me[t-2] == 0) {
      return 1;
    }
    
    else if (opponent[t-2] == 0 && opponent[t-1] == 0 && me[t-1] == 1 && me[t-2] == 0) {
      return 0;
    }

    else if (opponent[t-2] == 0 && opponent[t-1] == 1 && me[t-1] == 0 && me[t-2] == 0) {
      return 1;
    }

    else if (opponent[t-2] == 0 && opponent[t-1] == 1 && me[t-1] == 1 && me[t-2] == 0) {
      return 0;
    }

    else if (opponent[t-2] == 1 && opponent[t-1] == 0 && me[t-1] == 0 && me[t-2] == 0) {
      return 1;
    }
    
    else if (opponent[t-2] == 1 && opponent[t-1] == 0 && me[t-1] == 1 && me[t-2] == 0) {
      return 0;
    }
    
    else if (opponent[t-2] == 1 && opponent[t-1] == 1 && me[t-1] == 0 && me[t-2] == 0) {
      return 1;
    }
    
    else if (opponent[t-2] == 1 && opponent[t-1] == 1 && me[t-1] == 1 && me[t-2] == 0) {
      return 0;
    }

    else if (opponent[t-2] == 0 && opponent[t-1] == 0 && me[t-1] == 0 && me[t-2] == 1) {
      return 1;
    }
    
    else if (opponent[t-2] == 0 && opponent[t-1] == 0 && me[t-1] == 1 && me[t-2] == 1) {
      return 0;
    }

    else if (opponent[t-2] == 0 && opponent[t-1] == 1 && me[t-1] == 0 && me[t-2] == 1) {
      return 1;
    }

    else if (opponent[t-2] == 0 && opponent[t-1] == 1 && me[t-1] == 1 && me[t-2] == 1) {
      return 0;
    }

    else if (opponent[t-2] == 1 && opponent[t-1] == 0 && me[t-1] == 0 && me[t-2] == 1) {
      return 1;
    }
    
    else if (opponent[t-2] == 1 && opponent[t-1] == 0 && me[t-1] == 1 && me[t-2] == 1) {
      return 0;
    }
    
    else if (opponent[t-2] == 1 && opponent[t-1] == 1 && me[t-1] == 0 && me[t-2] == 1) {
      return 1;
    }
    
    else if (opponent[t-2] == 1 && opponent[t-1] == 1 && me[t-1] == 1 && me[t-2] == 1) {
      return 0;
    }

    return 0; // otherwise cooperate
  }

  return chooseAction;
}


strategies[cid + '10c'] = function () {
  var a = 1, b = 0, temp, num = 10;
  
  function chooseAction(me, opponent, t) {
    // Fiboncci

    while (num >= 0){
      if ( (a/t) == 1){
        return 1;
      }
      temp = a;
      a = a + b;
      b = temp;
      num--;
    }

    return 0;
  }
    return chooseAction;
}



strategies[cid + '200a'] = function () {
  var a = 1, b = 0, temp, num = 200;
  
  function chooseAction(me, opponent, t) {
    // Fiboncci

    while (num >= 0){
      if ( (a/t) == 1){
        return 1;
      }
      temp = a;
      a = a + b;
      b = temp;
      num--;
    }

    return 0;
  }
    return chooseAction;
}


strategies[cid + '200b'] = function () {
  // evil is a state variable for this strategy.
  // The initialization code ('var evil = false;'') will be run
  // before each game, so the variable evil will always equal
  // false when the game starts.

  var evil = false; // start out as not evil

  function chooseAction(me, opponent, t) {
    // This strategy uses the state variable 'evil'.
    // In every round, turn evil with 5% probability.
    // (And remain evil until the 200 rounds are over.)
    if (Math.random() < 0.05) {
      evil = true;
    }

    // If evil, defect
    if (evil) return 0;

    return 1; // and cooperate otherwise
  }
  return chooseAction;
}


strategies[cid + '200c'] = function () {
  var a = 1, b = 0, temp, num = 10;
  
  function chooseAction(me, opponent, t) {
    // Fiboncci

    while (num >= 0){
      if ( (a/t) == 1){
        return 1;
      }
      temp = a;
      a = a + b;
      b = temp;
      num--;
    }

    return 0;
  }
    return chooseAction;
}


strategies[cid + '200mistakes'] = function () {
  var a = 1, b = 0, temp, num = 200;
  
  function chooseAction(me, opponent, t) {
    // Fiboncci

    while (num >= 0){
      if ( (a/t) == 1){
        return 1;
      }
      temp = a;
      a = a + b;
      b = temp;
      num--;
    }

    return 0;
  }
    return chooseAction;
}

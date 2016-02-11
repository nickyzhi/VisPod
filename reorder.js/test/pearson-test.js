require("science");
require("../reorder.v1");

var vows = require("vows"),
    assert = require("assert");

var suite = vows.describe("reorder.pearson");

suite.addBatch({
    "pearson": {
	"simple": function() {
	    var a = [1, 2, 3, 4, 5], b = [5, 4, 3, 2, 1];

	    assert.equal(reorder.correlation.pearson(a, b), -1);
	},
	"harder": function() {
	    var a = [0.38906616,  0.5773394 ,  0.17349286,  0.5540746,
		     0.93085356, 0.91643792,  0.85663005,  0.15666242,
		     0.91411063,  0.50854478],
		b = [0.2845388 ,  0.08112363,  0.81855562,  0.12360082,
		     0.96107274, 0.78954847,  0.05820312,  0.34101782,
		     0.62052291,  0.25681059],
		y = reorder.correlation.pearson(a, b),
		e = 0.21706031819808619;
	    //console.log('y = '+y+', e='+e);
	    assert.inDelta(y, e, 0.00001);
	},
	"hard": function() {
	    var X = [[ 0.6813319 ,  0.90478228,  0.11681552,
		       0.2879309 ,  0.91980914],
		     [ 0.86943635,  0.63710069,  0.3685353,
		       0.39660358,  0.58182883],
		     [ 0.7097419 ,  0.25265316,  0.2377928 ,
		       0.1065309 ,  0.00203621],
		     [ 0.18564092,  0.6546422 ,  0.06249554,
		       0.94448868,  0.3452618 ]],
		E = [[ 0.        ,  0.67610163,  0.02692672,  0.07496238],
		     [ 0.67610163,  0.        ,  0.73793422, -0.25448483],
		     [ 0.02692672,  0.73793422,  0.        , -0.41270574],
		     [ 0.07496238, -0.25448483, -0.41270574,  0.        ]],
		Y = reorder.correlation.pearsonMatrix(X);
	    assert.inDeltaArray(Y, E, 0.00001);
	}
    }
});

suite.export(module);


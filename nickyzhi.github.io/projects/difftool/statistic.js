

function findMaxSubStr(s1,s2){ 
    var str= "",
        L1=s1.length,
        L2=s2.length; 
    
    if (L1>L2){ 
        var s3=s1;
        s1=s2;
        s2=s3;
        s3 = null;
        L1=s2.length;
        L2=s1.length;
    }
    
    
    for (var i=L1; i > 0; i--) {
        for (var j= 0; j <= L2 - i && j < L1; j++){ 
            str = s1.substr(j, i);
            if (s2.indexOf(str) >= 0) {
                return str; 
            }
        } 
    }
    
    return ""; 
}

function diff (s1,s2){
    var a = s1.split(" ");
    var b = s2.split(" ");
    var aLen = a.length ;
    var bLen = b.length ;
    PlusResult = [];
    MinusResult = [];
    for (var i = 0 ; i < bLen ; i ++){
        if (a.indexOf (b[i ]) == -1 ){
            MinusResult .push (b[i ]);
         }
    }
    for (var i = 0 ; i < aLen ; i ++){
        if (b.indexOf (a[i ]) == -1 ){
            PlusResult .push (a[i ]);
         }
    }
    return [PlusResult,MinusResult];
}

function levenshtein(s1, s2) {
    // init
    var d = [],
        m = s1.length,
        n = s2.length,
        i, j,cost;
    for (i = 0; i <= m; i++) {
        d[i] = [];
        d[i][0] = i;
    }
    for (j = 0; j <= n; j++) {
        d[0][j] = j;
    }
    
    for (j = 1; j <= n; j++) {
        for (i = 1; i <= m; i++) {
            if (s1[i] === s2[j]) {
                cost = 0;
            } 
            else {
                cost =1;
            }
            d[i][j] = Math.min(
                    d[i - 1][j] + 1, // a deletion
                    d[i][j - 1] + 1, // an insertion
                    d[i - 1][j - 1] + cost // a substitution
                )
        }
    }
    
    return d[m][n];
}

function similarity(a, b) {
    var s1 = a.split(" ");
    var s2 = b.split(" ");
    return 1 - levenshtein(s1, s2) / Math.max(s1.length, s2.length);
};
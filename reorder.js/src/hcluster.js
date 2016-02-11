if (typeof science == "undefined") {
    science = {version: "1.9.1"}; // semver [jdf] should be defined
    science.stats = {};
}

science.stats.hcluster = function() {
  var distance = reorder.distance.euclidean,
      linkage = "single", // single, complete or average
      distMatrix = null;

  function hcluster(vectors) {
    var n = vectors.length,
        dMin = [],
        cSize = [],
//        distMatrix = [],
        clusters = [],
        c1,
        c2,
        c1Cluster,
        c2Cluster,
        p,
        root,
        i,
        j,
	id = 0;

    // Initialise distance matrix and vector of closest clusters.
      if (distMatrix === null) {
	  distMatrix = [];
	  i = -1; while (++i < n) {
	      dMin[i] = 0;
	      distMatrix[i] = [];
	      j = -1; while (++j < n) {
		  distMatrix[i][j] = i === j ? Infinity : distance(vectors[i] , vectors[j]);
		  if (distMatrix[i][dMin[i]] > distMatrix[i][j]) dMin[i] = j;
	      }
	  }
      }
      else {
	  if (distMatrix.length < n || distMatrix[0].length < n)
	      throw {error: "Provided distance matrix length "+distMatrix.length+" instead of "+n};
	  i = -1; while (++i < n) {
	      dMin[i] = 0;
	      j = -1; while (++j < n) {
		  if (i === j)
		      distMatrix[i][j] = Infinity;
		  if (distMatrix[i][dMin[i]] > distMatrix[i][j]) dMin[i] = j;
	      }
	  }
      }
    // create leaves of the tree
    i = -1; while (++i < n) {
	if (i != id) console.log("i = %d, id = %d", i, id);
      clusters[i] = [];
      clusters[i][0] = {
        left: null,
        right: null,
        dist: 0,
        centroid: vectors[i],
	id: id++, //[jdf] keep track of original data index
        size: 1,
        depth: 0
      };
      cSize[i] = 1;
    }

    // Main loop
    for (p = 0; p < n-1; p++) {
      // find the closest pair of clusters
      c1 = 0;
      for (i = 0; i < n; i++) {
        if (distMatrix[i][dMin[i]] < distMatrix[c1][dMin[c1]]) c1 = i;
      }
      c2 = dMin[c1];

      // create node to store cluster info 
      c1Cluster = clusters[c1][0];
      c2Cluster = clusters[c2][0];

      var newCluster = {
        left: c1Cluster,
        right: c2Cluster,
        dist: distMatrix[c1][c2],
        centroid: calculateCentroid(c1Cluster.size, c1Cluster.centroid,
          c2Cluster.size, c2Cluster.centroid),
	id: id++,
        size: c1Cluster.size + c2Cluster.size,
        depth: 1 + Math.max(c1Cluster.depth, c2Cluster.depth)
      };
      clusters[c1].splice(0, 0, newCluster);
      cSize[c1] += cSize[c2];

      // overwrite row c1 with respect to the linkage type
      for (j = 0; j < n; j++) {
        switch (linkage) {
          case "single":
            if (distMatrix[c1][j] > distMatrix[c2][j])
              distMatrix[j][c1] = distMatrix[c1][j] = distMatrix[c2][j];
            break;
          case "complete":
            if (distMatrix[c1][j] < distMatrix[c2][j])
              distMatrix[j][c1] = distMatrix[c1][j] = distMatrix[c2][j];
            break;
          case "average":
            distMatrix[j][c1] = distMatrix[c1][j] = (cSize[c1] * distMatrix[c1][j] + cSize[c2] * distMatrix[c2][j]) / (cSize[c1] + cSize[j]);
            break;
        }
      }
      distMatrix[c1][c1] = Infinity;

      for (i = 0; i < n; i++)
        distMatrix[i][c2] = distMatrix[c2][i] = Infinity;

      // update dmin and replace ones that previous pointed to c2 to point to c1
      for (j = 0; j < n; j++) {
        if (dMin[j] == c2) dMin[j] = c1;
        if (distMatrix[c1][j] < distMatrix[c1][dMin[c1]]) dMin[c1] = j;
      }

      // keep track of the last added cluster
      root = newCluster;
    }

    return root;
  }

  hcluster.linkage = function(x) {
    if (!arguments.length) return linkage;
    linkage = x;
    return hcluster;
  };

  hcluster.distance = function(x) {
    if (!arguments.length) return distance;
    distance = x;
    return hcluster;
  };

  hcluster.distanceMatrix = function(x) {
    if (!arguments.length) return distMatrix;
    distMatrix = x.map(function(y) { return y.slice(0); });
    return hcluster;
  };

  return hcluster;
};

function calculateCentroid(c1Size, c1Centroid, c2Size, c2Centroid) {
  var newCentroid = [],
      newSize = c1Size + c2Size,
      n = c1Centroid.length,
      i = -1;
  while (++i < n) {
    newCentroid[i] = (c1Size * c1Centroid[i] + c2Size * c2Centroid[i]) / newSize;
  }
  return newCentroid;
}

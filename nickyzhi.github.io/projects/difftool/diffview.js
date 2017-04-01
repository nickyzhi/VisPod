
diffview = {
	/**
	 * Builds and returns a visual diff view.  The single parameter, `params', should contain
	 * the following values:
	 *
	 * - baseTextLines: the array of strings that was used as the base text input to SequenceMatcher
	 * - newTextLines: the array of strings that was used as the new text input to SequenceMatcher
	 * - opcodes: the array of arrays returned by SequenceMatcher.get_opcodes()
	 * - baseTextName: the title to be displayed above the base text listing in the diff view; defaults
	 *	   to "Base Text"
	 * - newTextName: the title to be displayed above the new text listing in the diff view; defaults
	 *	   to "New Text"
	 * - contextSize: the number of lines of context to show around differences; by default, all lines
	 *	   are shown
	 * - viewType: if 0, a side-by-side diff view is generated (default); if 1, an inline diff view is
	 *	   generated
	 */
	buildView: function (params) {
		var baseTextLines = params.baseTextLines;
		var newTextLines = params.newTextLines;
		var opcodes = params.opcodes;
		var baseTextName = params.baseTextName ? params.baseTextName : "Base Text";
		var newTextName = params.newTextName ? params.newTextName : "New Text";
		var contextSize = params.contextSize;
		var inline = false;

		if (baseTextLines == null)
			throw "Cannot build diff view; baseTextLines is not defined.";
		if (newTextLines == null)
			throw "Cannot build diff view; newTextLines is not defined.";
		if (!opcodes)
			throw "Canno build diff view; opcodes is not defined.";

		function celt (name, clazz) {
			var e = document.createElement(name);
			e.className = clazz;
			return e;
		}

		function telt (name, text) {
			var e = document.createElement(name);
			e.appendChild(document.createTextNode(text));
			return e;
		}

		function ctelt (name, clazz, text) {
			var e = document.createElement(name);
			e.className = clazz;
			e.appendChild(document.createTextNode(text));
			return e;
		}

		function ctelt_compare (name, clazz, text,text2) {
			var e = document.createElement(name);
			e.className = clazz;
			e.appendChild(document.createTextNode(text));
			e.onclick= function () {
								analyze_pair(text,text2);
			};
			return e;
		}

		var tdata = document.createElement("thead");

		var node = document.createElement("tr");
		tdata.appendChild(node);


		node.appendChild(document.createElement("th"));
		node.appendChild(ctelt("th", "texttitle", baseTextName));
		node.appendChild(ctelt("th", "texttitle", newTextName));

		tdata = [tdata];

		var rows = [];
		var node2;

		/**
		 * Adds two cells to the given row; if the given row corresponds to a real
		 * line number (based on the line index tidx and the endpoint of the
		 * range in question tend), then the cells will contain the line number
		 * and the line of text from textLines at position tidx (with the class of
		 * the second cell set to the name of the change represented), and tidx + 1 will
		 * be returned.	 Otherwise, tidx is returned, and two empty cells are added
		 * to the given row.
		 */
		function addCells (row, tidx, tend, textLines, change) {
			if (tidx < tend) {
				row.appendChild(telt("th", (tidx+1).toString()));
				row.appendChild(ctelt("td", change, textLines[tidx].replace(/\t/g, "\u00a0\u00a0\u00a0\u00a0")));
				return tidx + 1;
			}
			else {
				row.appendChild(document.createElement("th"));
				row.appendChild(celt("td", "empty"));
				return tidx;
			}
		}

		function analyze_pair(text1,text2) {
				var spa = " ";
				var res1 = text1.concat(spa);
				var res2 = res1.concat(text2);

				var thisIsAnObject = {res2};
				window.textVariable = thisIsAnObject;
				sessionStorage.setItem("text1", text1);
				sessionStorage.setItem("text2", text2);
				window.location = 'analyze.html'

	  }

		function addCells_compare (row, tidx, tend, textLines, change,textLines2) {
			if (tidx < tend) {
				row.appendChild(telt("th", (tidx+1).toString()));
				row.appendChild(ctelt_compare("td", change, textLines[tidx].replace(/\t/g, "\u00a0\u00a0\u00a0\u00a0"),textLines2[tidx].replace(/\t/g, "\u00a0\u00a0\u00a0\u00a0")));
				return tidx + 1;
			}
			else {
				row.appendChild(document.createElement("th"));
				row.appendChild(celt("td", "empty"));
				return tidx;
			}
		}

		function addCells_compare2 (row, tidx, tend, textLines, change,textLines2) {
			if (tidx < tend) {
				row.appendChild(ctelt_compare("td", change, textLines[tidx].replace(/\t/g, "\u00a0\u00a0\u00a0\u00a0"),textLines2[tidx].replace(/\t/g, "\u00a0\u00a0\u00a0\u00a0")));
				return tidx + 1;
			}
			else {
				row.appendChild(document.createElement("th"));
				row.appendChild(celt("td", "empty"));
				return tidx;
			}
		}

		for (var idx = 0; idx < opcodes.length; idx++) {
			code = opcodes[idx];
			change = code[0];
			var b = code[1];
			var be = code[2];
			var n = code[3];
			var ne = code[4];
			var rowcnt = Math.max(be - b, ne - n);
			var toprows = [];
			var botrows = [];
			for (var i = 0; i < rowcnt; i++) {
				// jump ahead if we've alredy provided leading context or if this is the first range
				if (contextSize && opcodes.length > 1 && ((idx > 0 && i == contextSize) || (idx == 0 && i == 0)) && change=="equal") {
					var jump = rowcnt - ((idx == 0 ? 1 : 2) * contextSize);
					if (jump > 1) {
						toprows.push(node = document.createElement("tr"));

						b += jump;
						n += jump;
						i += jump - 1;
						node.appendChild(telt("th", "..."));
						if (!inline) node.appendChild(ctelt("td", "skip", ""));
						node.appendChild(telt("th", "..."));
						node.appendChild(ctelt("td", "skip", ""));

						// skip last lines if they're all equal
						if (idx + 1 == opcodes.length) {
							break;
						} else {
							continue;
						}
					}
				}

				toprows.push(node = document.createElement("tr"));
				b = addCells_compare(node, b, be, baseTextLines, change, newTextLines);
				n = addCells_compare2(node, n, ne, newTextLines, change, baseTextLines);
			}

			for (var i = 0; i < toprows.length; i++) rows.push(toprows[i]);
			for (var i = 0; i < botrows.length; i++) rows.push(botrows[i]);
		}

		rows.push(node = ctelt("th", "author", "Diff view generated by "));
		node.setAttribute("colspan", inline ? 3 : 4);
		node.appendChild(node2 = telt("a", "HCI GoGrad Team"));

		tdata.push(node = document.createElement("tbody"));
		for (var idx in rows) rows.hasOwnProperty(idx) && node.appendChild(rows[idx]);

		node = celt("table", "diff" + (inline ? " inlinediff" : ""));
		for (var idx in tdata) tdata.hasOwnProperty(idx) && node.appendChild(tdata[idx]);
		return node;
	}
};

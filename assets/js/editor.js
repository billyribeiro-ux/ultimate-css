/* PE7 CSS Course — live HTML/CSS editor
   Vanilla JS, zero dependencies. Finds every .editor block and wires it.
*/
(() => {
  const editors = document.querySelectorAll(".editor");
  editors.forEach(init);

  function init(root) {
    const htmlArea = root.querySelector('[data-editor="html"]');
    const cssArea  = root.querySelector('[data-editor="css"]');
    const frame    = root.querySelector('[data-editor="preview"]');
    const runBtn   = root.querySelector('[data-editor-action="run"]');
    const resetBtn = root.querySelector('[data-editor-action="reset"]');

    if (!frame || (!htmlArea && !cssArea)) return;

    const initial = {
      html: htmlArea ? htmlArea.value : "",
      css:  cssArea  ? cssArea.value  : ""
    };

    let timer = null;
    const schedule = () => {
      if (timer) clearTimeout(timer);
      timer = setTimeout(render, 250);
    };

    function render() {
      const html = htmlArea ? htmlArea.value : "";
      const css  = cssArea  ? cssArea.value  : "";
      const doc =
        "<!doctype html><html><head><meta charset='utf-8'>" +
        "<style>html,body{margin:0;padding:1rem;font-family:system-ui,sans-serif;color:#111}" +
        "*{box-sizing:border-box}</style>" +
        "<style>" + css + "</style></head><body>" + html + "</body></html>";
      frame.srcdoc = doc;
      frame.classList.remove("editor-flash");
      void frame.offsetWidth;
      frame.classList.add("editor-flash");
    }

    function reset() {
      if (htmlArea) htmlArea.value = initial.html;
      if (cssArea)  cssArea.value  = initial.css;
      render();
    }

    [htmlArea, cssArea].forEach(ta => {
      if (!ta) return;
      ta.addEventListener("input", schedule);
      ta.addEventListener("keydown", onKey);
    });
    if (runBtn)   runBtn.addEventListener("click", render);
    if (resetBtn) resetBtn.addEventListener("click", reset);

    render();
  }

  function onKey(e) {
    const ta = e.currentTarget;
    if (e.key === "Tab" && !e.ctrlKey && !e.metaKey) {
      e.preventDefault();
      const start = ta.selectionStart;
      const end   = ta.selectionEnd;
      if (e.shiftKey) {
        // Outdent: remove up to 2 leading spaces from the current line
        const before = ta.value.slice(0, start);
        const lineStart = before.lastIndexOf("\n") + 1;
        const line = ta.value.slice(lineStart, end);
        const stripped = line.replace(/^ {1,2}/, "");
        ta.value = ta.value.slice(0, lineStart) + stripped + ta.value.slice(end);
        const diff = line.length - stripped.length;
        ta.selectionStart = Math.max(lineStart, start - diff);
        ta.selectionEnd   = Math.max(lineStart, end - diff);
      } else {
        ta.value = ta.value.slice(0, start) + "  " + ta.value.slice(end);
        ta.selectionStart = ta.selectionEnd = start + 2;
      }
      ta.dispatchEvent(new Event("input", { bubbles: true }));
    } else if (e.key === "Escape") {
      ta.blur();
    }
  }
})();

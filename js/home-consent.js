(function () {
    "use strict";

    var GREEN = "#0b6b4a";
    var RED = "#c0392b";
    var MARK = "mpa-consent-style";

    function injectCSS() {
        if (document.getElementById(MARK)) return;
        var css = [
            /* poora box click target hai */
            ".mpa-consent{cursor:pointer;transition:border-color .15s,background .15s;" +
                "-webkit-tap-highlight-color:transparent;}",
            ".mpa-consent:hover{border-color:rgba(0,0,0,.28);}",
            ".mpa-consent.is-on{border-color:" + GREEN + ";background:#f4fbf8;}",
            ".mpa-consent.is-bad{border-color:" + RED + ";background:#fff7f7;}",

            /* checkbox thoda bada aur clear */
            ".mpa-consent-row input{width:18px!important;height:18px!important;" +
                "min-width:18px!important;min-height:18px!important;margin:1px 0 0!important;" +
                "accent-color:" + GREEN + ";cursor:pointer;}",
            ".mpa-consent-row input:focus-visible{outline:2px solid " + GREEN + ";outline-offset:2px;}",

            /* links box ke click ke upar rehne chahiye */
            ".mpa-consent a{position:relative;z-index:2;}",

            /* error line */
            ".mpa-consent-err{display:none;margin:8px 0 0;font-size:12px;font-weight:700;color:" + RED + ";}",
            ".mpa-consent.is-bad .mpa-consent-err{display:block;}"
        ].join("");
        var s = document.createElement("style");
        s.id = MARK;
        s.textContent = css;
        document.head.appendChild(s);
    }

    function boxOf(el) {
        return el.closest ? el.closest(".mpa-consent") : null;
    }

    function cbOf(box) {
        return box.querySelector(".mpa-consent-box, input[type=checkbox]");
    }

    function paint(box) {
        var cb = cbOf(box);
        if (!cb) return;
        box.classList.toggle("is-on", cb.checked);
        if (cb.checked) box.classList.remove("is-bad");
    }

    function setup(box) {
        if (box.getAttribute("data-mpa-ready")) return;
        box.setAttribute("data-mpa-ready", "1");

        var cb = cbOf(box);
        if (!cb) return;

        if (!box.querySelector(".mpa-consent-err")) {
            var e = document.createElement("p");
            e.className = "mpa-consent-err";
            e.textContent = "Aage badhne ke liye consent par tick karein.";
            box.appendChild(e);
        }

        box.addEventListener("click", function (ev) {
            if (ev.target.closest("a")) return;                 // Privacy / Terms
            if (ev.target === cb) { paint(box); return; }       // checkbox khud
            if (ev.target.closest("label")) { paint(box); return; } // label native
            cb.checked = !cb.checked;
            cb.dispatchEvent(new Event("change", { bubbles: true }));
            paint(box);
        });
        cb.addEventListener("change", function () { paint(box); });

        /* pichhli baar tick kiya tha to yaad rakho */
        try {
            if (localStorage.getItem("premium_home_consent") === "1") cb.checked = true;
        } catch (err) { /* private mode */ }
        paint(box);
    }

    /* consent bina form submit na ho */
    function guard() {
        document.addEventListener("submit", function (ev) {
            var form = ev.target;
            if (!form || !form.querySelector) return;
            var box = form.querySelector(".mpa-consent");
            if (!box) return;
            var cb = cbOf(box);
            if (!cb || cb.checked) {
                try { localStorage.setItem("premium_home_consent", "1"); } catch (e) {}
                return;
            }
            ev.preventDefault();
            ev.stopPropagation();
            box.classList.add("is-bad");
            box.scrollIntoView({ behavior: "smooth", block: "center" });
            cb.focus();
        }, true);
    }

    function init() {
        injectCSS();
        var boxes = document.querySelectorAll(".mpa-consent");
        for (var i = 0; i < boxes.length; i++) setup(boxes[i]);
        guard();
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }
})();

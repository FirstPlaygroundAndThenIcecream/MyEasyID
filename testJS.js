<h1 id="demo"> SKAT </h1><br>
    <iframe src="http://80.210.70.4:3333/easyid-form.php" width="300" height="350" frameborder="0" allowfullscreen>
    </iframe>
    <p id="customerMsg"></p>
    <script>
        document.getElementById("demo").innerHTML = "Hello Skat!";
        if (window.addEventListener) {
            window.addEventListener("message", onMessage, false);        
        } 
        else if (window.attachEvent) {
            window.attachEvent("onmessage", onMessage, false);
        }

        function onMessage(event) {
            // Check sender origin to be trusted
            if (event.origin !== "http://80.210.70.4:3333") return;

            var data = event.data;

            if (typeof(window[data.func]) == "function") {
                window[data.func].call(null, data.message);
            }
        }

        // Function to be called from iframe
        function parentFunc(message) {
            alert(message);
            loadDoc(message);
        }

        function loadDoc(message) {
            document.getElementById("customerMsg").innerHTML = message;
        }

    </script>
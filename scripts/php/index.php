<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="assets/css/main_style.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div class="container-search">
            <div class="container-search-titile">
                <h1>Hello, There!</h1>
            </div>
            <div class="container-search-input">
                <form method="post" action="index.php">

                    <!-- Input the Link -->
                    <div class="form-url">
                        <label>What Website so you want to scan?</label>
                        <input class="form-url-input" name="url" type="url" placeholder="Enter the URL">
                    </div>
                    <div class="form-keyphrase">                    
                        <label>What phrase are you looking for?</label>
                        <input name="keyphrase" type="text" placeholder="Enter the key phrase in the search">
                    </div>
                    <div>
                        <!-- PDF DOCS OR XLS -->
                        <label>Select a Format</label>
                        <select name="format">
                            <option value="keyphrase">Key phrase</option>
                            <option value="pdf">PDF File</option>
                            <option value="word">Word File</option>
                            <option value="excel">Excel File</option>
                        </select>
                    </div>

                    <div>
                        <!-- is it in title, link, or files -->
                        <label>Select where would you like to search for a KeyWord</label>
                        <select name="filter">
                            <option value="intitle">In the Title</option>
                            <option value="inurl">In the URL</option>
                            <option value="inwebpage">On the WebSite</option>
                        </select>
                    </div>

                    <!-- submit the data and start the search -->
                    <button style="height: 30px; width: 50px;" type="submit">Submit</button>

                </form>
            </div>
            <div class="container-search-output">
                <!-- <div class="container-search-output-link">
                    <a class="link-output" href="https://youtu.be/dQw4w9WgXcQ?si=hJT4n5ROzmx8jC3J">https://youtu.be/dQw4w9WgXcQ?si=hJT4n5ROzmx8jC3J</a>
                    <button>Download</button>
                </div>
                <div class="container-search-output-link">
                    <a class="link-output" href="https://youtu.be/dQw4w9WgXcQ?si=hJT4n5ROzmx8jC3J">https://youtu.be/dQw4w9WgXcQ?si=hJT4n5ROzmx8jC3J</a>
                    <button>Download</button>
                </div>
                <div class="container-search-output-link">
                    <a class="link-output" href="https://youtu.be/dQw4w9WgXcQ?si=hJT4n5ROzmx8jC3J">https://youtu.be/dQw4w9WgXcQ?si=hJT4n5ROzmx8jC3J</a>
                    <button>Download</button>
                </div>
                <div class="container-search-output-link">
                    <a class="link-output" href="https://youtu.be/dQw4w9WgXcQ?si=hJT4n5ROzmx8jC3J">https://youtu.be/dQw4w9WgXcQ?si=hJT4n5ROzmx8jC3J</a>
                    <button>Download</button>
                </div>
                <div class="container-search-output-link">
                    <a class="link-output" href="https://youtu.be/dQw4w9WgXcQ?si=hJT4n5ROzmx8jC3J">https://youtu.be/dQw4w9WgXcQ?si=hJT4n5ROzmx8jC3J</a>
                    <button>Download</button> -->
                </div>
            </div>
        </div>
    </div>
</body>
</html>

<?php
    try{    
        if($_SERVER["REQUEST_METHOD"] == "POST"){
            $link = $_POST['url'];
            $format = $_POST['format'];
            $filter = $_POST['filter'];
            $keyphrase = $_POST['keyphrase'];

            // echo "<div class='container-search-output-link'> <a class='link-output' href='https://youtu.be/dQw4w9WgXcQ?si=hJT4n5ROzmx8jC3J'>$link</a><button>Download</button></div><a href='$link'>$link</a>" . '<br>';
            // echo"$link". "<br>";
            // echo "$filter" . "<br>"; 
            // echo "\n$keyphrase". "<br>";

            $setup_file = fopen("meta.json","w");  // scripts\data\meta.json;

            $send_data = new stdClass();
            $send_data -> url = "$link";
            $send_data -> format = "$format";
            $send_data -> option = "$filter";       // this is the filter for the search;
            $send_data -> phrase = "$keyphrase";
            
            //echo gettype($send_data);

            $send_data_json = json_encode($send_data);


            fwrite($setup_file,$send_data_json);
            fclose($setup_file);
            
            $json_data = fopen("scraphed.json","r"); // scripts\data\scraped.json;
            $data = fread($json_data,filesize("scraphed.json"));
        
            fclose($json_data);

            $data = json_decode($data);
            echo gettype($data);
            $keys = array_keys((array)$data);

            $value = array();
            $arr = get_object_vars($data);

            foreach($arr as $ar ){
                $value[] = $ar;
            }
            echo $value[0];
            for ($i = 0; $i < count($keys); $i++ ){
                echo "<div class='container-search-output-link'> <a class='link-output' href='$keys[$i]'>$value[$i]</a><button>Download</button></div>";
            }
        
        }
    }
    catch(error){
        echo"$error";
    }

?>
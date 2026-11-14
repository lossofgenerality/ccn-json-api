(* Wolfram Language client for the CCN JSON API.
   Local Mathematica/Wolfram Engine: use the localhost URL.
   Wolfram Cloud: use your public Vercel URL (localhost is not reachable).
   © Computational Classnotes · CC BY-NC-SA 4.0 *)

apiURL = "http://localhost:8000/api";
(* apiURL = "https://YOUR-PROJECT.vercel.app/api"; *)

callAPI[data_Association] := URLExecute[
  HTTPRequest[apiURL, <|
    "Method" -> "POST",
    "ContentType" -> "application/json",
    "Body" -> ExportString[data, "RawJSON"]
  |>],
  "RawJSON"
];

callAPI[<|"message" -> "hi"|>]
(* <|"ok" -> True, "result" -> "I am here"|> *)

callAPI[<|"message" -> "hi"|>]["result"]
(* "I am here" *)

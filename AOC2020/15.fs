printfn "Advent of Code 2020 Day 15"



// let filespec = "sample.day14.txt"
// let filespec = "sample2.day14.txt"
// let filespec = "input.day14.txt"
//let lines = System.IO.File.ReadAllLines(filespec) |> Array.toList
// let lines =  Array.map int lines1 

// let lines = lines1 |> Array.map (fun c -> c.ToCharArray() )

let startinput = [|6;4;12;1;20;0;16|]
// let startinput = [|0;3;6|]
// let startinput = [|1;3;2|]
// let startinput = [|2;1;3|]
// let startinput = [|1;2;3|]
// let startinput = [|2;3;1|]
// let startinput = [|3;2;1|]
// let startinput = [|3;1;2|]

open System.Collections.Generic
let mutable tracknumbers = new Dictionary<int, int option * int option >()

let dump (tracknumbers:Dictionary<int,(int option * int option)>) =
    printfn "\nDump tracknumbers"
    for i in tracknumbers.Keys do
        let a,b = tracknumbers.[i]
        match a,b with
            | Some x, Some y -> printfn "# %d %d - %d " i x y
            | None , Some y -> printfn "# %d N/A - %d " i  y
            | None , None  -> printfn "# %d N/A - N/A " i
            | _   -> printfn "# %d FAIL %A " i (a,b)

// let tmp:int = tracknumbers

let travel   i spoke =
    match i,spoke  with
         | 5,_    -> printfn "   # %4d s:%d " i spoke 
         | 2020,_ -> printfn "   # %4d s:%d " i spoke
         | 2021,_ -> printfn "   # %4d s:%d " i spoke         
         | 30000000,_ -> printfn "   # %4d s:%d " i spoke
         | _ -> ()
        
    let found, value = tracknumbers.TryGetValue spoke
    // printfn "           %d %A %d " i found spoke
    match found, value with
            | true, (Some x, Some y) -> // printfn "# %d %d - %d s:%d" i x y spoke
                                        tracknumbers.[spoke] <- ( Some y, Some i )
                                        i - y
            | true, (None  , Some y) -> // printfn "# %d N/A - %d s:%d " i  y spoke
                                        tracknumbers.[spoke] <- ( Some y, Some i )
                                        i - y

            | false, _               -> // printfn "# %d - first time s:%d" i spoke
                                        tracknumbers.[spoke] <- ( None  , Some i )
                                        0
            | _  -> 0




let mutable speak = 0
let mutable counts = 1
for s in startinput do
    speak <- travel counts s
    counts <- counts + 1

for ii in counts ..( counts+30000000)  do
    speak <- travel  ii speak

// dump tracknumbers

(*
                     part 2
                     
 Microsoft (R) F# Compiler version 4.1
Copyright (c) Microsoft Corporation. All Rights Reserved.
time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono 15.exe
Advent of Code 2020 Day 15
   #    5 s:20 
   # 2020 s:475 
   # 2021 s:0 
   # 30000000 s:11261   - part 2 CORRECT
       12.29 real        14.20 user         0.50 sys

Compilation finished at Mon Dec 14 22:50:08
*)

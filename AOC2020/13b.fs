printfn "Advent of Code 2020 Day 13"
// Day 13



// let filespec = "sample2.day13.txt"
// let filespec = "input.day13.txt"
// let lines1 = System.IO.File.ReadAllLines(filespec) 
// let lines =  Array.map (fun c -> if c = "x" then 0 else (int c) ) lines1 

// let lines = lines1 |> Array.map (fun c -> c.ToCharArray() )





let goal = 1000391
let busids = [| 13 ;17;19;23;29;37;383;41;457|]

// let filespec = "sample.day13.txt"
// let goal = 939
// let busids = [|7;13;59;31;19|]

// printfn "%A" busids


let lm x =
    let s = goal / x
    if (s * x) = goal then goal,x else ( s + 1 ) * x,x

let sorted = busids |> Array.map lm |> Array.sort

let answer=((fst sorted.[0]) - goal ) * (snd sorted.[0])

// printfn "Part1_%s: Answer %d %A  (1915)" filespec answer sorted

(*
           That's not the right answer. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 1000396.) [Return to Day 13]


Compilation started at Sat Dec 12 21:12:27

make -k 13.exe
/Library/Frameworks/Mono.framework/Versions/Current/bin/fsharpc 13.fs
Microsoft (R) F# Compiler version 4.1
Copyright (c) Microsoft Corporation. All Rights Reserved.
time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono 13.exe
Advent of Code 2020 Day 13
[|13; 17; 19; 23; 29; 37; 383; 41; 457|]
Part1_sample.day13.txt: Answer 1000396 [|1000396; 1000399; 1000400; 1000402; 1000406; 1000407; 1000408; 1000413;
  1000830|]  ()
        0.11 real         0.09 user         0.01 sys

Compilation finished at Sat Dec 12 21:12:30


           sample works now
make -k 13.exe
/Library/Frameworks/Mono.framework/Versions/Current/bin/fsharpc 13.fs
Microsoft (R) F# Compiler version 4.1
Copyright (c) Microsoft Corporation. All Rights Reserved.
time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono 13.exe
Advent of Code 2020 Day 13
[|7; 13; 59; 31; 19|]
Part1_sample.day13.txt: Answer 295 [|(944, 59); (945, 7); (949, 13); (950, 19); (961, 31)|]  ()
        0.12 real         0.10 user         0.01 sys

Compilation finished at Sat Dec 12 21:16:32


make -k 13.exe
/Library/Frameworks/Mono.framework/Versions/Current/bin/fsharpc 13.fs
Microsoft (R) F# Compiler version 4.1
Copyright (c) Microsoft Corporation. All Rights Reserved.
time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono 13.exe
Advent of Code 2020 Day 13
[|13; 17; 19; 23; 29; 37; 383; 41; 457|]
Part1_sample.day13.txt: Answer 1915 [|(1000396, 383); (1000399, 17); (1000400, 41); (1000402, 13); (1000406, 37);
  (1000407, 19); (1000408, 23); (1000413, 29); (1000830, 457)|]  ()
        0.12 real         0.10 user         0.01 sys

Compilation finished at Sat Dec 12 21:17:10
           
           *)

// part 2
// let busids = [| 13 ;17;19;23;29;37;383;41;457|]
// let filespec = "input.day13.txt"           
let busdeps = [|"19";"x";"x";"x";"x";"x";"x";"x";"x";"x";"x";"x";"x";"37";"x";"x";"x";"x";"x";"383";"x";"x";"x";"x";"x";"x";"x";"23";"x";"x";"x";"x";"13";"x";"x";"x";"x";"x";"x";"x";"x";"x";"x";"x";"x";"x";"x";"x";"29";"x";"457";"x";"x";"x";"x";"x";"x";"x";"x";"x";"41";"x";"x";"x";"x";"x";"x";"17" |]

let filespec = "sample.day13.txt"

// let busdeps = [|"7";"13";"x";"x";"59";"x";"31";"19" |]
(*
The earliest timestamp that matches the list 17,x,13,19 is 3417.
67,7,59,61 first occurs at timestamp 754018.
67,x,7,59,61 first occurs at timestamp 779210.
67,7,x,59,61 first occurs at timestamp 1261476.
1789,37,47,1889 first occurs at timestamp 1202161486.
*)

// let busdeps = [|"67";"7";"59";"61"|] //  first occurs at timestamp 754018.

// let busdeps = [|"67";"x";"7";"59";"61"|] // first occurs at timestamp 779210.

// let busdeps = [|"67";"7";"x";"59";"61"|] //  first occurs at timestamp 1261476.

// let busdeps = [|"1789";"37";"47";"1889"|] // first occurs at timestamp 1202161486.

let businput = seq {
    let mutable offset = -1
    for b in busdeps do
       offset <- offset + 1
       if b = "x"
       then () // yield 0,0
       else yield (int64 b), int64 offset

   }

let b2 = businput |> Seq.toList   
let z64 = int64 0

for i in businput do
    if (fst i) > z64 then printfn "%A" i

let is_valid (bi: (int64*int64) list) (x:int64) = bi |> List.forall (fun (bid, tick) -> (x +  tick) %  bid = z64 )

// printfn "%A" b2
// let _is_valid (bi: (int*int) list) (x :int64) =
//     let mutable result = true
//     for bid,tick in bi do
//         printfn "%d %d %A" bid tick (x + int64 tick)
//         if (x + int64 tick) % (int64 bid) = (int64 0) then () else result <- false
//     result

let submain minfor limitfor =
    let maxbid = int64 (b2 |> List.map (fun c -> (fst c) ) |> List.max )
    let mutable maxtick = int64 0
    for bid,tick in b2 do
        if (int64 bid) =  maxbid then maxtick <- int64 tick

    printfn "Max Busid   %d , %d " maxbid maxtick
    printfn "range \n%A\n%A  " minfor limitfor

    //    let minfor = 99999999999551L + 8399999999774L // add 10 minutes that we already ran
    // let limitfor = (int64 210000000000000L)
    //     let limitfor = minfor + 120000000000000L
    for (i:int64) in minfor..maxbid..limitfor do
        // printfn "%d" i
        if is_valid b2 (i - maxtick)
        then printfn "part2: input %A (1068781) FOUND" (i - maxtick)
        if i % 119999999592L  = z64 then printfn "%A" i

    printfn "is_valid %A %d " (is_valid b2 1068781L)  (1068781 % 59)
    printfn "Part2_%s: Answer %d %A   ()" filespec answer businput


[<EntryPoint>]
let main args =
    printfn "Arguments passed to function : %A" args
    if args.Length > 0 then submain (int64 args.[0])  (int64 args.[1])
    // Return 0. This indicates success.
    0

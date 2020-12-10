printfn "Advent of Code 2020 Day 10"
// Day 10


let lines1 = System.IO.File.ReadAllLines("input.day10.txt")

// let lines1 = System.IO.File.ReadAllLines("sample.day10.txt")
// let mydev = 22 // sample

// let lines1 = System.IO.File.ReadAllLines("sample2.day10.txt")
// let mydev = 52 // sample2

// let lines1 = System.IO.File.ReadAllLines("sample3.day10.txt")
// let mydev = 14 // sample2

// let lines = Array.concat [ [| 0 |] ; Array.map int lines1 ]
let lines =  Array.map int lines1 

let slines = lines |> Array.sort 
// printfn "%A" slines
let endi = slines.Length - 1
let part1notthesum = 3 + (Array.map2  (fun i1 i0 -> i1 - i0 )  slines.[1..endi]  slines.[0..( endi - 1 ) ] |> Array.sum)

let ones = (Array.map2  (fun i1 i0 -> if (i1 - i0 = 1) then 1 else 0 )  slines.[1..endi]  slines.[0..( endi - 1 ) ] |> Array.sum)

let threes = 1 + (Array.map2  (fun i1 i0 -> if (i1 - i0 = 3) then 1 else 0 )  slines.[1..endi]  slines.[0..( endi - 1 ) ] |> Array.sum)
// let part1sum  = 3 + (slines.[1..endi]  |> Array.iteri (fun i -> slines.[ i ] - slines.[ i - 1 ] ) |> Array.sum )


let part1sum = ones * threes
printfn "Day10 part1 %d %d %d " part1sum  ones threes


(*
           -*- mode: compilation; default-directory: "~/MoonBaseAlpha/AOC2020/" -*-
Compilation started at Wed Dec  9 22:05:46

make  aoc20_day10.exe
/Library/Frameworks/Mono.framework/Versions/Current/bin/fsharpc aoc20_day10.fs
Microsoft (R) F# Compiler version 4.1
Copyright (c) Microsoft Corporation. All Rights Reserved.
time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono aoc20_day10.exe
Advent of Code 2020 Day 10
Day10 part1 1690 65 26 
        0.08 real         0.06 user         0.01 sys

Compilation finished at Wed Dec  9 22:05:49

           *)

(*
          part2
          find all the elements that before after are <= 3
          
          *)

// let addpermutations i =
//     let a = slines.[i+1] - slines.[i]
//     let b = slines.[i+2] - slines.[i]
//     let c = slines.[i+3] - slines.[i]
//     let p = match a,b,c with
//             | 1,2,3 -> 4
//             | 1,2,_ -> 2
//             | 1,3,_ -> 2
//             | 2,3,_ -> 2
//             | _,_,_ -> 1
//     printfn "%d %d %d -> %d" a b c p
//     p

// let advance i =
//     let a = slines.[i+1] - slines.[i]
//     let b = slines.[i+2] - slines.[i]
//     let c = slines.[i+3] - slines.[i]
//     let p = match a,b,c with
//             | 1,2,3 -> 2
//             | 1,2,_ -> 1
//             | _,_,_ -> 1
//     printfn "           adv %d %d %d -> %d" a b c p
//     p
    
// // let part2 = [0.. (endi - 3)] |> List.map addpermutations 
// // printfn "Day10 part2 %A " part2

// let mutable i = 0
// let mutable part2sum = 1

// while i < endi - 3 do
//     part2sum <- part2sum * (addpermutations i)
//     i <- i + (advance i)
    


// printfn "Day10 part2 %A " part2sum


// let is_valid ( data : int array ) i j =
//      [ (i + 1 ) ..j] |> List.forall  (fun c -> (data.[c] - data.[c-1]) <= 3)

let is_valid ( data : int list )  =
     // printfn "%A" ( data |> Seq.windowed 2 ) 
     data |> Seq.windowed 2 |> Seq.forall  (fun c -> c.[1] - c.[0] <= 3)

let is_valid10 ( data : int list )  =
     // printfn "%A" ( data |> Seq.windowed 2 ) 
     if (data |> Seq.windowed 2 |> Seq.forall  (fun c -> c.[1] - c.[0] <= 3)) then 1 else 0

// printfn "is valid %A " (is_valid slines 0 (endi-1))

// let rec brute_force data i j =
//     if (is_valid data i j)
//     then
//         1
//     else
//          0

let rec gen_seq (data :int list) = seq {
    if is_valid data
    then
        if data.Length = 1
        then
           yield data
           yield []
        else
           for i in gen_seq data.[1..] do
              yield i
              yield data.[0] :: i
    else
        yield [-99;99]
        }


let rec gen_seq_fixed_ends (data :int list) =
    let permenant = data.Head
    let endpoint = data.[ data.Length - 1 ]
    seq {
        for i in gen_seq data.[1..(data.Length - 2)] do
            yield permenant::i @ [endpoint]
    }

// for i in slines do
//    printfn "%A" i

// for j in gen_seq  [1;2;3;4] do
//     let testlist = j
//     printfn "%A %A" testlist (is_valid testlist)


// for j in gen_seq ( slines |> Array.toList ) do
//     let testlist = 0::j
//     if is_valid testlist then printfn "%A %A" testlist (is_valid testlist)

let mini_brute0 data =
    //    printfn "%A" (gen_seq data |> Seq.map (fun ll -> 0::ll) )
    gen_seq data |> Seq.map (fun ll -> 0::ll) |>  Seq.sumBy is_valid10

let mini_brute (data: int list)  =
    // printfn "%A" (gen_seq_fixed_ends data )
    if data.Length = 2
    then int64 1
    else int64 (gen_seq_fixed_ends data |>  Seq.sumBy is_valid10)

// printfn "%d" (mini_brute (slines |> Array.toList))


    
// printfn "%A" (gen_seq_fixed_ends [ 0;1;2;3;4;5;8 ])

let rec index3 (slines : int list ) start =
    if (slines.[ start + 1 ] - slines.[start] = 3 ) then start + 1 else index3 slines (start + 1 )

let mutable start = 0
let mutable answers = (int64 1)

let fulldata = 0 :: (slines |>Array.toList) @  [slines.[slines.Length - 1] + 3]
// let fulldata = 0 :: slines @ [slines.[slines.Length - 1] + 3]
// printfn "fulldata %d %A" fulldata.Length fulldata
let mutable three = 0


while three < (fulldata.Length - 1) do
    three <- index3 fulldata start
    printfn "Run from %d to %d" start three
    let variations = mini_brute fulldata.[start..three]
    answers <- answers * variations
    printfn "Run from %d to %d so far * %d => %d " start three variations answers
    start <- three

printfn " Part2 %d (5289227976704) " answers
(*

Compilation started at Thu Dec 10 02:49:08

make  aoc20_day10.exe
/Library/Frameworks/Mono.framework/Versions/Current/bin/fsharpc aoc20_day10.fs
Microsoft (R) F# Compiler version 4.1
Copyright (c) Microsoft Corporation. All Rights Reserved.
time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono aoc20_day10.exe
Advent of Code 2020 Day 10
[|1; 2; 3; 4; 7; 8; 11; 12; 13; 14; 15; 18; 19; 20; 21; 24; 25; 26; 27; 28; 31;
  32; 33; 34; 35; 38; 39; 40; 41; 44; 47; 50; 51; 52; 55; 56; 57; 58; 61; 64; 65;
  66; 67; 70; 71; 72; 73; 76; 77; 78; 79; 80; 83; 84; 85; 86; 89; 90; 91; 92; 93;
  96; 99; 100; 101; 102; 103; 106; 107; 108; 111; 112; 113; 114; 115; 118; 119;
  120; 121; 122; 125; 128; 129; 132; 133; 134; 135; 138; 139; 140|]
Day10 part1 1664 64 26 
fulldata 92 [0; 1; 2; 3; 4; 7; 8; 11; 12; 13; 14; 15; 18; 19; 20; 21; 24; 25; 26; 27; 28; 31;
 32; 33; 34; 35; 38; 39; 40; 41; 44; 47; 50; 51; 52; 55; 56; 57; 58; 61; 64; 65;
 66; 67; 70; 71; 72; 73; 76; 77; 78; 79; 80; 83; 84; 85; 86; 89; 90; 91; 92; 93;
 96; 99; 100; 101; 102; 103; 106; 107; 108; 111; 112; 113; 114; 115; 118; 119;
 120; 121; 122; 125; 128; 129; 132; 133; 134; 135; 138; 139; 140; 143]
Run from 0 to 5
Run from 0 to 5 so far * 7 => 7 
Run from 5 to 7
Run from 5 to 7 so far * 1 => 7 
Run from 7 to 12
Run from 7 to 12 so far * 7 => 49 
Run from 12 to 16
Run from 12 to 16 so far * 4 => 196 
Run from 16 to 21
Run from 16 to 21 so far * 7 => 1372 
Run from 21 to 26
Run from 21 to 26 so far * 7 => 9604 
Run from 26 to 30
Run from 26 to 30 so far * 4 => 38416 
Run from 30 to 31
Run from 30 to 31 so far * 1 => 38416 
Run from 31 to 32
Run from 31 to 32 so far * 1 => 38416 
Run from 32 to 35
Run from 32 to 35 so far * 2 => 76832 
Run from 35 to 39
Run from 35 to 39 so far * 4 => 307328 
Run from 39 to 40
Run from 39 to 40 so far * 1 => 307328 
Run from 40 to 44
Run from 40 to 44 so far * 4 => 1229312 
Run from 44 to 48
Run from 44 to 48 so far * 4 => 4917248 
Run from 48 to 53
Run from 48 to 53 so far * 7 => 34420736 
Run from 53 to 57
Run from 53 to 57 so far * 4 => 137682944 
Run from 57 to 62
Run from 57 to 62 so far * 7 => 963780608 
Run from 62 to 63
Run from 62 to 63 so far * 1 => 963780608 
Run from 63 to 68
Run from 63 to 68 so far * 7 => 6746464256 
Run from 68 to 71
Run from 68 to 71 so far * 2 => 13492928512 
Run from 71 to 76
Run from 71 to 76 so far * 7 => 94450499584 
Run from 76 to 81
Run from 76 to 81 so far * 7 => 661153497088 
Run from 81 to 82
Run from 81 to 82 so far * 1 => 661153497088 
Run from 82 to 84
Run from 82 to 84 so far * 1 => 661153497088 
Run from 84 to 88
Run from 84 to 88 so far * 4 => 2644613988352 
Run from 88 to 91
Run from 88 to 91 so far * 2 => 5289227976704 
 Part2 5289227976704
        0.18 real         0.14 user         0.01 sys

Compilation finished at Thu Dec 10 02:49:11
*)

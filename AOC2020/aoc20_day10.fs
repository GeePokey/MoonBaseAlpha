printfn "Advent of Code 2020 Day 10"
// Day 10


// let lines1 = System.IO.File.ReadAllLines("input.day10.txt")

// let lines1 = System.IO.File.ReadAllLines("sample.day10.txt")
// let mydev = 22 // sample

// let lines1 = System.IO.File.ReadAllLines("sample2.day10.txt")
// let mydev = 52 // sample2

let lines1 = System.IO.File.ReadAllLines("sample3.day10.txt")
let mydev = 14 // sample2

// let lines = Array.concat [ [| 0 |] ; Array.map int lines1 ]
let lines =  Array.map int lines1 

let slines = lines |> Array.sort
printfn "%A" slines
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
           yield data.[0]::[mydev;]
           yield [mydev;]
        else
           for i in gen_seq data.[1..] do
              yield i
              yield data.[0] :: i
    else
        yield [-99;99]
        }

// for i in slines do
//    printfn "%A" i

// for j in gen_seq  [1;2;3;4] do
//     let testlist = j
//     printfn "%A %A" testlist (is_valid testlist)


for j in gen_seq ( slines |> Array.toList ) do
    let testlist = 0::j
    if is_valid testlist then printfn "%A %A" testlist (is_valid testlist)

let mini_brute data =
    //    printfn "%A" (gen_seq data |> Seq.map (fun ll -> 0::ll) )
    gen_seq data |> Seq.map (fun ll -> 0::ll) |>  Seq.sumBy is_valid10

printfn "%d" (mini_brute (slines |> Array.toList))


    


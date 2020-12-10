printfn "Advent of Code 2020 Day 10"
// Day 10


let lines1 = System.IO.File.ReadAllLines("input.day10.txt")

// let lines1 = System.IO.File.ReadAllLines("sample.day10.txt")
// let lines1 = System.IO.File.ReadAllLines("sample2.day10.txt")

let lines = Array.concat [ [| 0 |] ; Array.map int lines1 ]

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

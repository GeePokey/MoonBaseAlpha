printfn "Advent of Code 2020 Day 9"
// Day 9


let lines1 = System.IO.File.ReadAllLines("input.day9.txt")
let tailsize = 25
let goal = (int64 20874512)

// let lines1 = System.IO.File.ReadAllLines("sample.day9.txt")
// let tailsize = 5
// let goal = (int64 127)
let lines = Array.map int64 lines1



// printfn "%A" lines

// for i in lines do
//    printfn "%d" i

// for i in [0..(lines.Length-1)]  do
//     printfn "%3d %d" i lines.[i]
// printfn "end dump input\n"

let containsNumber number list7 = Array.exists (fun elem -> elem = number) list7

let is_valid (list25: int64 array) (value :int64) =

    let debugvar =  [list25 |> Array.map (fun x -> value - x)]
    // printfn "value %d  %A" value debugvar
    Array.exists (fun x -> not (value - x = x ) && containsNumber (value - x) list25) list25



for i in [tailsize..(lines.Length - 1)] do
    // printfn "check %d %d " i lines.[i] 
    // printfn "check %d %d %A" i lines.[i] lines.[(i - tailsize)..(i - 1)]
    if (not (is_valid lines.[(i - tailsize)..(i - 1)] lines.[i]))
    then printfn "Part1 not found %d %d (20874512)" i lines.[i]
    

(*

part1
999 25770962344753
end dump input

not found 537 20874512
        0.77 real         0.12 user         0.01 sys

Compilation finished at Tue Dec  8 21:45:10

Part1 not found 537 20874512 (20874512)
        0.13 real         0.10 user         0.01 sys

Compilation finished at Tue Dec  8 21:46:28

 *)


// Part2


let mutable start = 0
let mutable stop = 1
let mutable progress = (int64(lines.[start] + lines.[stop]))

while not (progress = goal) && (stop < lines.Length) do
    if progress < goal
    then
        stop <- stop + 1
        progress <- progress + lines.[stop]
    else
        progress <- progress - lines.[start]
        start <- start + 1

printfn "Part2 range start %d stop %d goal %d = %d min=%d max=%d sum = %d (3012420)" start stop goal (Array.sum lines.[start..stop]) (Array.min lines.[start..stop])  (Array.max lines.[start..stop]) ((Array.min lines.[start..stop]) +  (Array.max lines.[start..stop]))


(*
         Advent of Code 2020 Day 9
Part1 not found 537 20874512 (20874512)
range start 424 stop 440 goal 20874512 = 20874512 min=925549 max=2086871 sum = 3012420
        0.10 real         0.08 user         0.01 sys

Compilation finished at Tue Dec  8 22:03:35


-*- mode: compilation; default-directory: "~/MoonBaseAlpha/AOC2020/" -*-
Compilation started at Tue Dec  8 22:04:20

make  aoc20_day9.exe
/Library/Frameworks/Mono.framework/Versions/Current/bin/fsharpc aoc20_day9.fs
Microsoft (R) F# Compiler version 4.1
Copyright (c) Microsoft Corporation. All Rights Reserved.
time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono aoc20_day9.exe
Advent of Code 2020 Day 9
Part1 not found 537 20874512 (20874512)
Part2 range start 424 stop 440 goal 20874512 = 20874512 min=925549 max=2086871 sum = 3012420 (3012420)
        0.09 real         0.07 user         0.01 sys

Compilation finished at Tue Dec  8 22:04:23

         *)

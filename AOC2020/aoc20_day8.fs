printfn "Advent of Code 2020 Day 8"
// Day 8
let lines1 = System.IO.File.ReadAllLines("input.day8.txt")
// let lines1 = System.IO.File.ReadAllLines("sample.day8.txt")
let lines = Array.append lines1  [|"eof +0"|] 



printfn "%A" lines

for i in lines do
    printfn "%s" i
    
(*
        acc increases or decreases a single global value called the
        accumulator by the value given in the argument. For example,
        acc +7 would increase the accumulator by 7. The accumulator
        starts at 0. After an acc instruction, the instruction
        immediately below it is executed next.  

        jmp jumps to a new instruction relative to itself. The next
        instruction to execute is found using the argument as an
        offset from the jmp instruction; for example, jmp +2 would
        skip the next instruction, jmp +1 would continue to the
        instruction immediately below it, and jmp -20 would cause the
        instruction 20 lines above to be executed next.  

        nop stands for No OPeration - it does nothing. The instruction
        immediately below it is executed next.

        *)


open System.Text.RegularExpressions

let (|Regex|_|) pattern input =
    let m = Regex.Match(input, pattern)
    if m.Success then Some(List.tail [ for g in m.Groups -> g.Value ])
    else None

let mutable accum = 0
let mutable pc = 0

let mutable running = true
let mutable visitedpc = Set.empty

let runonce flipped =
    // printfn "flipped %d" flipped
    let mutable eofreached = false
    if lines.[flipped].[0..2] = "acc" then eofreached <- false
    else
        accum <- 0
        running <- true
        pc <- 0
        visitedpc <- Set.empty

        // printfn "flip %d %s" flipped lines.[flipped]
        while running do

            let virtualline = if flipped = pc
                              then ( if lines.[pc].[0..2]="nop" then "jmp" else "nop" ) + lines.[pc].[3..]
                              else lines.[pc] 
            match virtualline with
                | Regex @"(nop) ([+-][\d]+)" [operation; value] -> ()
                | Regex @"(acc) ([+-][\d]+)" [operation; value] -> accum <- accum + (int value)
                | Regex @"(jmp) ([+-][\d]+)" [operation; value] -> pc <- pc + (int value) - 1
                | Regex @"(eof) ([+-][\d]+)" [operation; value] -> printfn "EOF reached !! @ %d accum = %d  flipped #%d  Part2 (631)\n" pc accum flipped
                                                                   running <- false
                                                                   eofreached <- true
                | _ -> printfn "Bad instruction at %d" pc
                       running <- false
            pc <- pc + 1
            if visitedpc.Contains pc
            then
                printfn "Loop case at %d accum = %d" pc accum
                running <- false
            else
                visitedpc <- visitedpc.Add(pc)

    eofreached          
let proglen = Seq.length lines
printfn "%d" proglen

for i in [0..proglen] do
    runonce i
    
(* sample case running
/Library/Frameworks/Mono.framework/Versions/Current/bin/fsharpc aoc20_day8.fs
Microsoft (R) F# Compiler version 4.1
Copyright (c) Microsoft Corporation. All Rights Reserved.
time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono aoc20_day8.exe
Advent of Code 2020 Day 8
[|"nop +0"; "acc +1"; "jmp +4"; "acc +3"; "jmp -3"; "acc -99"; "acc +1";
  "jmp -4"; "acc +6"|]
Loop case at 1 accum = 5
        0.15 real         0.13 user         0.01 sys

Compilation finished at Mon Dec  7 21:20:02

Right answer Part 1 !!

Loop case at 479 accum = 1818
        0.15 real         0.13 user         0.01 sys

Compilation finished at Mon Dec  7 21:21:09




Loop case at 479 accum = 988
EOF reached !! @ 636 accum = 631  flipped #429
Loop case at 479 accum = 1818

Comint exited abnormally with code 2 at Mon Dec  7 21:55:38

*)

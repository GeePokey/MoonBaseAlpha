printfn "Advent of Code 2020 Day 6"
// Day 6
let lines = System.IO.File.ReadAllLines("input.day6.txt") 
// let lines = System.IO.File.ReadAllLines("D4_kinput.txt") 
// let lines = System.IO.File.ReadAllLines("input.txt")
//let lines = System.IO.File.ReadAllLines("sample.day6.txt") 
// printfn "%A" lines

let len = lines |> Seq.length
let width = lines.[0] |> Seq.length


// Improved Part1 after submit:
let rec validate1 input (groupquestionsaccum: string List) total  =
    match input with
        | ""::tail -> validate1 tail [] (total + (groupquestionsaccum |> Seq.map Set.ofSeq |> Set.unionMany ).Count )
        | h::tail  -> validate1 tail (h::groupquestionsaccum) total 
        | []       -> total


// Part 2
let rec validate2 input (groupquestionsaccum: string List) total  =
    // printfn "%A %A %A" input groupquestionsaccum total
    match input with
        | ""::tail -> validate2 tail [] (total + (groupquestionsaccum |> Seq.map Set.ofSeq |> Set.intersectMany ).Count )
        | h::tail  -> validate2 tail (h::groupquestionsaccum) total 
        | []       -> total


// Orig part 1
        
let rec sub_validate groupcustomform  accum  =
   match groupcustomform with
       | h::tail  -> // printfn "sub validate %A" h
                     sub_validate tail (Set.union  (h |> Set.ofSeq ) accum )
       | []  -> accum.Count


 
let rec validate1_orig input (groupquestionsaccum: string List) total  =
    match input with
        | ""::tail -> validate1_orig tail [] (total + (sub_validate  groupquestionsaccum Set.empty ) )
        | h::tail  -> validate1_orig tail (h::groupquestionsaccum) total 
        | []       -> total


// Part1
// byr (Birth Year)
// iyr (Issue Year)
// eyr (Expiration Year)
// hgt (Height)
// hcl (Hair Color)
// ecl (Eye Color)
// pid (Passport ID)
// cid (Country ID)

(*
end of passport 0xFE gooder 
end of list
containtest true
        0.56 real         0.12 user         0.01 sys

Compilation finished at Thu Dec  3 21:58:27

245 "good"
*)

// Part 2

open System.Text.RegularExpressions

let (|Regex|_|) pattern input =
    let m = Regex.Match(input, pattern)
    if m.Success then Some(List.tail [ for g in m.Groups -> g.Value ])
    else None

    // //Example:
    // let phone = "(555) 555-5555"
    // match phone with
    // | Regex @"\(([0-9]{3})\)[-. ]?([0-9]{3})[-. ]?([0-9]{4})" [ area; prefix; suffix ] ->
    //     printfn "Area: %s, Prefix: %s, Suffix: %s" area prefix suffix
    // | _ -> printfn "Not a phone number"


// Part 2

// 02 byr (Birth Year) - four digits; at least 1920 and at most 2002.
// 04 iyr (Issue Year) - four digits; at least 2010 and at most 2020.
// 08 eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
// 10 hgt (Height) - a number followed by either cm or in:
// If cm, the number must be at least 150 and at most 193.
// If in, the number must be at least 59 and at most 76.
// 20 hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
// 40 ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
// 80 pid (Passport ID) - a nine-digit number, including leading zeroes.
// cid (Country ID) - ignored, missing or not.

let rec monovalidate2 (s:string) =
     // printfn " monovalidate %A %A %A " s ( s.Contains("byr:") )      (if s.Contains "byr:" then 0x02 else 0 )
    if s.Contains " "
    then s.Split(" ") |> Seq.map monovalidate2 |> Seq.sum
    else
        match s with
            | Regex @"byr:(\d\d\d\d)" [byr] when byr > "1919" && byr < "2003" ->  2 
            | Regex @"iyr:(\d\d\d\d)" [byr] when byr > "2009" && byr < "2021" ->  4
            | Regex @"eyr:(\d\d\d\d)" [byr] when byr > "2019" && byr < "2031" ->  8
            | Regex @"hgt:(\d\d\d)cm" [byr] when byr > "149"  && byr < "194"  ->  0x10
            | Regex @"hgt:(\d\d)in"   [byr] when byr > "58"   && byr < "77"   ->  0x10
            | Regex @"hcl:#([0-9a-f]{6})$"  [ma]                              ->  0x20
            | Regex @"ecl:(...)$"     [ma]  -> match ma with
                                                | "amb" -> 0x40
                                                | "blu" -> 0x40
                                                | "brn" -> 0x40
                                                | "gry" -> 0x40
                                                | "grn" -> 0x40
                                                | "hzl" -> 0x40
                                                | "oth" -> 0x40
                                                | _ -> // printfn "no match: %A %A" ma s
                                                       0
            | Regex @"pid:([\d]{9})$"  [ma]                                  -> 0x80
            | _  -> // printfn "no match: %A " s
                    0 // Regex @"cid:.*" -> 0



// Part1
printfn "Part1 %d " ( validate1 ( lines |> Seq.toList ) []  0 )


// Part2
printfn "Part2 %d " ( validate2 ( lines |> Seq.toList )  [] 0 )

printfn "\n"


(*
   guess 1 wrong

   Advent of Code 2020 Day 6
Part1 6487 
 Part 1 0 () 9: PM 
 Part 2 0 () 9: PM 


        0.10 real         0.07 user         0.01 sys

Compilation finished at Sun Dec  6 02:39:32
Advent of Code 2020 Day 6
Part1 6487 
 Part 1 0 () 9: PM 
 Part 2 0 () 9: PM 


        0.10 real         0.07 user         0.01 sys

Compilation finished at Sun Dec  6 02:39:32

   That's not the right answer; your answer is too low. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 6487.) [Return to Day 6]


// forgot the blank line at the end of input - I need to fix the reader loop.
   
That's the right answer! You are one gold star closer to saving your vacation. [Continue to Part Two]

-*- mode: compilation; default-directory: "~/MoonBaseAlpha/AOC2020/" -*-
Compilation started at Sun Dec  6 02:42:17

make -k aoc20_day6.exe
/Library/Frameworks/Mono.framework/Versions/Current/bin/fsharpc aoc20_day6.fs
Microsoft (R) F# Compiler version 4.1
Copyright (c) Microsoft Corporation. All Rights Reserved.
time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono aoc20_day6.exe
Advent of Code 2020 Day 6
Part1 6506 
 Part 1 0 () 9: PM 
 Part 2 0 () 9: PM 


        0.10 real         0.08 user         0.01 sys

Compilation finished at Sun Dec  6 02:42:20


-*- mode: compilation; default-directory: "~/MoonBaseAlpha/AOC2020/" -*-
Compilation started at Sun Dec  6 03:03:43

make -k aoc20_day6.exe
/Library/Frameworks/Mono.framework/Versions/Current/bin/fsharpc aoc20_day6.fs
Microsoft (R) F# Compiler version 4.1
Copyright (c) Microsoft Corporation. All Rights Reserved.
time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono aoc20_day6.exe
Advent of Code 2020 Day 6
Part1 6506 
Part2 3243 


        0.10 real         0.08 user         0.01 sys

Compilation finished at Sun Dec  6 03:03:47


That's the right answer! You are one gold star closer to saving your vacation.

You have completed Day 6! You can [Share] this victory or [Return to Your Advent Calendar].
   *)

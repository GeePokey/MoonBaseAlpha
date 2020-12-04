printfn "Advent of Code 2020 Day 4"
// Day 4
let lines = System.IO.File.ReadAllLines("input.day4.txt") 
// let lines = System.IO.File.ReadAllLines("input.txt")
// let lines = System.IO.File.ReadAllLines("part2.txt") 
printfn "%A" lines

let len = lines |> Seq.length
let width = lines.[0] |> Seq.length


printfn " Part 1 %d () 9: PM " 0
printfn " Part 2 %d () 9: PM " 0

printfn "\n"
let monovalidate (s:string) =
     // printfn " monovalidate %A %A %A " s ( s.Contains("byr:") )      (if s.Contains "byr:" then 0x02 else 0 ) 
     (if s.Contains "cid:" then 0x01 else 0 ) |||
     (if s.Contains "byr:" then 0x02 else 0 ) |||
     (if s.Contains "iyr:" then 0x04 else 0 ) ||| 
     (if s.Contains "eyr:" then 0x08 else 0 ) ||| 
     (if s.Contains "hgt:" then 0x10 else 0 ) ||| 
     (if s.Contains "hcl:" then 0x20 else 0 ) ||| 
     (if s.Contains "ecl:" then 0x40 else 0 ) ||| 
     (if s.Contains "pid:" then 0x80 else 0 ) 



let rec sub_validate passport accum =
   match passport with
       | h::tail  -> // printfn "sub validate %A" h
                     sub_validate tail (accum  ||| (monovalidate h))
       | []  -> printfn "end of passport 0x%02X %s " accum ( if (accum &&& 0xFE) = 0xFE then "good" else "bad" )
                accum
   accum

 
let rec validate1 input paccum =
    match input with
        | ""::tail -> sub_validate paccum 0 
                      validate1 tail []
                      // printfn "a blank line"
                      ()
        | h::tail  -> validate1 tail (h::paccum)
                      // printfn "a passport line: %A " h
                      ()
        
        | []       -> printfn "end of list"
        


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

// // byr (Birth Year) - four digits; at least 1920 and at most 2002.
// // iyr (Issue Year) - four digits; at least 2010 and at most 2020.
// // eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
// // hgt (Height) - a number followed by either cm or in:
// // If cm, the number must be at least 150 and at most 193.
// // If in, the number must be at least 59 and at most 76.
// // hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
// // ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
// // pid (Passport ID) - a nine-digit number, including leading zeroes.
// // cid (Country ID) - ignored, missing or not.

// let rec monovalidate2 (s:string) =
//      // printfn " monovalidate %A %A %A " s ( s.Contains("byr:") )      (if s.Contains "byr:" then 0x02 else 0 )
//     if s.Contains " "
//     then s.Split(" ") |> Seq.map monovalidate2 |> Seq.sum
//     else
//         let fields = s.Split(":")
//         let token = fields.[0]
//         let value = fields.[1]
           
//         //         (if token.Contains "cid" then 0x00 else 0 ) |||
//         (if token.Contains "byr"
//                     then match System.Int32.TryParse value with
//                           | true,x -> if x >= 1920 && x <= 2002 then 2 else 0
//                           | _ -> 0
//                     else 0 ) ||| 
//         (if token.Contains "iyr"
//                 then 
//                   match System.Int32.TryParse value with
//                   | true,x -> if x >= 2010 && x <= 2020 then 0x04 else 0
//                   | _ -> 0
//                 else 0 ) ||| 
//         (if token.Contains "eyr"
//                   match System.Int32.TryParse value with
//                   | true,x -> if x >= 2020 && x <= 2030 then 0x08 else 0
//                   | _ -> 0
//              else 0 ) ||| 
//         (if token.Contains "hgt"
//              then 0x10
//              else 0 ) ||| 
//         (if token.Contains "hcl"
//              then 0x20
//              else 0 ) ||| 
//         (if token.Contains "ecl"
//              then 0x40
//              else 0 ) ||| 
//         (if token.Contains "pid"
//              then 0x80
//              else 0 ) 

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
            | Regex @"byr:(\d\d\d\d)" [byr] -> let byri = int byr
                                               if byri >= 1920 && byri <= 2002 then 0x2 else 0
            | Regex @"iyr:(\d\d\d\d)" [byr] -> let byri = int byr
                                               if byri >= 2010 && byri <= 2020 then 0x4 else 0
            | Regex @"eyr:(\d\d\d\d)" [byr] -> let byri = int byr
                                               if byri >= 2020 && byri <= 2030 then 0x8 else 0
            | Regex @"hgt:(\d\d\d)cm" [cm] -> let cmi = int cm
                                              if cmi >= 150 && cmi <= 193 then 0x10 else 0
            | Regex @"hgt:(\d\d)in"  [ma] -> let i = int ma
                                             if i >= 59 && i <= 76 then 0x10 else 0
            | Regex @"hcl:#([0-9a-f]{6})$"  [ma] -> // printfn "hcl: %A %A" ma s
                                                    0x20
            | Regex @"ecl:(...)$"  [ma] -> match ma with
                                             | "amb" -> 0x40
                                             | "blu" -> 0x40
                                             | "brn" -> 0x40
                                             | "gry" -> 0x40
                                             | "grn" -> 0x40
                                             | "hzl" -> 0x40
                                             | "oth" -> 0x40
                                             | _ -> printfn "no match: %A %A" ma s
                                                    0
            | Regex @"pid:([\d]{9})$"  [ma] -> 0x80
            | _  -> printfn "no match: %A " s
                    0 // Regex @"cid:.*" -> 0

            
        // let fields = s.Split(":")
        // let token = fields.[0]
        // let value = fields.[1]
           
        // //         (if token.Contains "cid" then 0x00 else 0 ) |||
        // (if token.Contains "byr"
        //             then match System.Int32.TryParse value with
        //                   | true,x -> if x >= 1920 && x <= 2002 then 2 else 0
        //                   | _ -> 0
        //             else 0 ) ||| 
        // (if token.Contains "iyr"
        //         then 
        //           match System.Int32.TryParse value with
        //           | true,x -> if x >= 2010 && x <= 2020 then 0x04 else 0
        //           | _ -> 0
        //         else 0 ) ||| 
        // (if token.Contains "eyr"
        //           match System.Int32.TryParse value with
        //           | true,x -> if x >= 2020 && x <= 2030 then 0x08 else 0
        //           | _ -> 0
        //      else 0 ) ||| 
        // (if token.Contains "hgt"
        //      then 0x10
        //      else 0 ) ||| 
        // (if token.Contains "hcl"
        //      then 0x20
        //      else 0 ) ||| 
        // (if token.Contains "ecl"
        //      then 0x40
        //      else 0 ) ||| 
        // (if token.Contains "pid"
        //      then 0x80
        //      else 0 ) 
    


let rec sub_validate2 passport accum =
   match passport with
       | h::tail  -> // printfn "sub validate %A" h
                     sub_validate2 tail (accum  ||| (monovalidate2 h))
       | []  -> printfn "end of passport 0x%02X %s " accum ( if (accum &&& 0xFE) = 0xFE then "2good" else "2bad" )
                accum
   accum

 
let rec validate2 input paccum =
    match input with
        | ""::tail -> sub_validate2 paccum 0 
                      validate2 tail []
                      // printfn "a blank line"
                      ()
        | h::tail  -> validate2 tail (h::paccum)
                      // printfn "a passport line: %A " h
                      ()
        
        | []       -> printfn "end of list"
        

// Part1
validate1 ( lines |> Seq.toList ) ["fred"] 

// Part2
validate2 ( lines |> Seq.toList ) ["fred"] 

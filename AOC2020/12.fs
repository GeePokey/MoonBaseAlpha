printfn "Advent of Code 2020 Day 12"
// Day 12


// let lines1 = System.IO.File.ReadAllLines("input.day12.txt")
// let filespec = "sample.day12.txt"
let filespec = "input.day12.txt"
let lines = System.IO.File.ReadAllLines(filespec) |> Array.toList
// let lines =  Array.map int lines1 

// let lines = lines1 |> Array.map (fun c -> c.ToCharArray() )


// printfn "%A" lines


open System.Text.RegularExpressions

let (|Regex|_|) pattern input =
    let m = Regex.Match(input, pattern)
    if m.Success then Some(List.tail [ for g in m.Groups -> g.Value ])
    else None

let rec travel code x y d =
      match code with
        | h::tail -> match h with
                       | Regex @"N(\d+)" [parm] -> travel tail x (y - (int parm)) d
                       | Regex @"S(\d+)" [parm] -> travel tail x (y + (int parm)) d 
                       | Regex @"W(\d+)" [parm] -> travel tail (x - (int parm)) y d
                       | Regex @"E(\d+)" [parm] -> travel tail (x + (int parm)) y d
                       | Regex @"R(\d+)" [parm] -> travel tail x  y (((d + (int parm)) + 720) % 360 ) 
                       | Regex @"L(\d+)" [parm] -> travel tail x  y (((d - (int parm)) + 720) % 360 ) 
                       | Regex @"F(\d+)" [parm] -> match d with
                                                    |   0 -> travel tail (x + (int parm)) y d // east
                                                    |  90 -> travel tail x (y + (int parm)) d // south
                                                    | 180 -> travel tail (x - (int parm)) y d // west
                                                    | 270 -> travel tail x (y - (int parm)) d // north
                                                    | _ -> printfn "ERROR: bad direction %s %d" h d
                                                           x, y
                       | _ -> printfn "ERROR: bad instruction"
                              x, y
        | _ -> x, y

let final = travel lines 0 0 0
printfn "%s %A %d" filespec final ((fst final) + (snd final))

(*
 Advent of Code 2020 Day 12
input.day12.txt (74, 746) 820
        0.16 real         0.14 user         0.01 sys

Compilation finished at Fri Dec 11 22:53:12

                                                      *)

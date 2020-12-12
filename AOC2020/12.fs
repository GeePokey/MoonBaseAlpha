printfn "Advent of Code 2020 Day 12"
// Day 12


let filespec = "sample2.day12.txt"
// let filespec = "input.day12.txt"
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

let sgn x = match x with
               | z when z < 0 -> -1
               | z when z > 0 -> +1
               | 0 -> 0
               | _ -> 0


let rec Rtator degrees x y wx wy =
    if degrees = 0 then (wx, wy)
    else
        let md = degrees - 90

        let dx = wx - x
        let dy = wy - y
        match sgn dx, sgn dy with
            |  1,  1 -> Rtator md x y (x - dy)  (y + dx)
            | -1,  1 -> Rtator md x y (x - dy)  (y + dx)
            | -1, -1 -> Rtator md x y (x - dy)  (y + dx)
            |  1, -1 -> Rtator md x y (x - dy)  (y + dx)
            |  1,  0 -> Rtator md x y  x  (y + dx)
            | -1,  0 -> Rtator md x y  x  (y + dx)
            |  0,  1 -> Rtator md x y (x - dy)  y
            |  0, -1 -> Rtator md x y (x - dy)  y
            |  0,  0 -> Rtator md x y x  y


printfn "%A" (Rtator   0 0 0 10 10)
printfn "%A" (Rtator  90 0 0 10 10)
printfn "%A" (Rtator 180 0 0 10 10)
printfn "%A" (Rtator 270 0 0 10 10)
printfn "%A" (Rtator 360 0 0 10 10)
printfn "-"
printfn "%A" (Rtator   0 1000 0 1010 0)
printfn "%A" (Rtator  90 1000 0 1010 0)
printfn "%A" (Rtator 180 1000 0 1010 0)
printfn "%A" (Rtator 270 1000 0 1010 0)
printfn "%A" (Rtator 360 1000 0 1010 0)

let Ltator degrees x y wx wy =
    let dx = wx - x
    let dy = wy - y
    let mutable md = degrees
    while md > 0 do
      match sgn dx, sgn dy with
        |  1,  1 -> x - dy , y + dx
        | -1,  1 -> x - dy , y + dx
        | -1, -1 -> x - dy , y + dx
        |  1, -1 -> x - dy , y + dx
      md <- md - 90
      
                                                   
let rec travelp2 (code : string list) x y wx wy =
    
    printfn "%3d %3d %3d %3d : %5s"  x y wx wy    (if code.IsEmpty then "[]" else code.Head)
    match code with
        | h::tail -> match h with
                       | Regex @"N(\d+)" [parm] -> travelp2 tail x y wx (wy - (int parm)) 
                       | Regex @"S(\d+)" [parm] -> travelp2 tail x y wx (wy + (int parm)) 
                       | Regex @"W(\d+)" [parm] -> travelp2 tail x y (wx - (int parm)) wy 
                       | Regex @"E(\d+)" [parm] -> travelp2 tail x y (wx + (int parm)) wy 
                       | Regex @"L(\d+)" [parm] -> let dx = wx - x
                                                   let dy = wy - y
                                                   travelp2 tail x y (x+dy) (y-dx)
                       | Regex @"R(\d+)" [parm] -> let dx = wx - x 
                                                   let dy = wy - y
                                                   travelp2 tail x y (x-dy) (y+dx)
                       | Regex @"F(\d+)" [parm] -> let dx = (wx - x) * (int parm)
                                                   let dy = (wy - y) * (int parm)
                                                   travelp2 tail (x+dx) (y+dy) (wx+dx) (wy+dy)
                       | _ -> printfn "ERROR: bad instruction"
                              x, y
        | _ -> x, y

let finalp2 = travelp2 lines 0 0 10 -1
printfn "part2 %s %A %d" filespec finalp2 ((fst finalp2) + (snd finalp2))

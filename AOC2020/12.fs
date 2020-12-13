printfn "Advent of Code 2020 Day 12"
// Day 12


// let filespec = "sample.day12.txt"
// let filespec = "sample2.day12.txt"
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



// // Stealing from Marshall's degrees to absolute direction recursion - works!
// let rec travel code x y d =
//       match code with
//         | h::tail -> match h with
//                        | Regex @"N(\d+)" [parm] -> travel tail x (y - (int parm)) d
//                        | Regex @"S(\d+)" [parm] -> travel tail x (y + (int parm)) d 
//                        | Regex @"W(\d+)" [parm] -> travel tail (x - (int parm)) y d
//                        | Regex @"E(\d+)" [parm] -> travel tail (x + (int parm)) y d
//                        | Regex @"R(\d+)" [parm] -> travel tail x  y (((d + (int parm)) + 720) % 360 ) 
//                        | Regex @"L(\d+)" [parm] -> travel tail x  y (((d - (int parm)) + 720) % 360 ) 
//                        | Regex @"F(\d+)" [parm] -> match d with
//                                                     |   0 -> travel (("E"+parm)::tail) x y d
//                                                     |  90 -> travel (("S"+parm)::tail) x y d   // tail x (y + (int parm)) d // south
//                                                     | 180 -> travel (("W"+parm)::tail) x y d   //  tail (x - (int parm)) y d // west
//                                                     | 270 -> travel (("N"+parm)::tail) x y d   // tail x (y - (int parm)) d // north
//                                                     | _ -> printfn "ERROR: bad direction %s %d" h d
//                                                            x, y
//                        | _ -> printfn "ERROR: bad instruction"
//                               x, y
//         | _ -> x, y

let final = travel lines 0 0 0
printfn "Part1 %s %A %d (820) " filespec final ((abs (fst final)) + (abs (snd final)))

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


        
        // match sgn dx, sgn dy with
        //     |  1,  1 -> Rtator md x y (x - dy)  (y + dx)
        //     | -1,  1 -> Rtator md x y (x - dy)  (y + dx)
        //     | -1, -1 -> Rtator md x y (x - dy)  (y + dx)
        //     |  1, -1 -> Rtator md x y (x - dy)  (y + dx)
        //     |  1,  0 -> Rtator md x y  x  (y + dx)
        //     | -1,  0 -> Rtator md x y  x  (y + dx)
        //     |  0,  1 -> Rtator md x y (x - dy)  y
        //     |  0, -1 -> Rtator md x y (x - dy)  y
        //     |  0,  0 -> Rtator md x y x  y


// printfn "-\n"

// printfn "%A" (Rtator   0 0 0 10 10)
// printfn "%A" (Rtator  90 0 0 10 10)
// printfn "%A" (Rtator 180 0 0 10 10)
// printfn "%A" (Rtator 270 0 0 10 10)
// printfn "%A" (Rtator 360 0 0 10 10)

// printfn "-\n"
// printfn "%A" (Rtator   0 1000 0 1010 0)
// printfn "%A" (Rtator  90 1000 0 1010 0)
// printfn "%A" (Rtator 180 1000 0 1010 0)
// printfn "%A" (Rtator 270 1000 0 1010 0)
// printfn "%A" (Rtator 360 1000 0 1010 0)

// printfn "-\n"

// printfn "%A" (Ltator   0 0 0 10 10)
// printfn "%A" (Ltator  90 0 0 10 10)
// printfn "%A" (Ltator 180 0 0 10 10)
// printfn "%A" (Ltator 270 0 0 10 10)
// printfn "%A" (Ltator 360 0 0 10 10)
// printfn "-\n"
// printfn "%A" (Ltator   0 1000 0 1010 0)
// printfn "%A" (Ltator  90 1000 0 1010 0)
// printfn "%A" (Ltator 180 1000 0 1010 0)
// printfn "%A" (Ltator 270 1000 0 1010 0)
// printfn "%A" (Ltator 360 1000 0 1010 0)
// printfn "-\n"



let rec Rtator degrees x y wx wy =
    if degrees = 0 then (wx, wy)
    else
        let md = degrees - 90

        let dx = wx - x
        let dy = wy - y
        Rtator md x y (x - dy)  (y + dx)

let rec Ltator degrees x y wx wy = Rtator (360-degrees) x y wx wy


let rec travelp2 (code : string list) x y wx wy =
    
    // printfn "%3d %3d %3d %3d : %5s"  x y wx wy    (if code.IsEmpty then "[]" else code.Head)
    match code with
        | h::tail -> match h with
                       | Regex @"N(\d+)" [parm] -> travelp2 tail x y wx               (wy - (int parm)) 
                       | Regex @"S(\d+)" [parm] -> travelp2 tail x y wx               (wy + (int parm)) 
                       | Regex @"W(\d+)" [parm] -> travelp2 tail x y (wx - (int parm)) wy 
                       | Regex @"E(\d+)" [parm] -> travelp2 tail x y (wx + (int parm)) wy 
                       | Regex @"L(\d+)" [parm] -> let wx,wy = Ltator (int parm) x y wx wy
                                                   travelp2 tail x y wx wy
                       | Regex @"R(\d+)" [parm] -> let wx,wy = Rtator (int parm) x y wx wy
                                                   travelp2 tail x y wx wy
                       | Regex @"F(\d+)" [parm] -> let dx = (wx - x) * (int parm)
                                                   let dy = (wy - y) * (int parm)
                                                   travelp2 tail (x+dx) (y+dy) (wx+dx) (wy+dy)
                       | _ -> printfn "ERROR: bad instruction"
                              x, y
        | _ -> x, y

let fx1,fy1 = travelp2 lines 0 0 10 -1
let fx = abs fx1
let fy = abs fy1
printfn "part2 %s (%d %d) (%d %d) = MD %d (66614) " filespec fx1 fy1 fx fy (fx + fy)


(*
 part2 sample.day12.txt (214, 72) 286
 0.18 real         0.15 user         0.01 sys

Compilation finished at Sat Dec 12 00:13:36



========================================================================================
    
-32041 34573 -32069 34524 :    []
part2 input.day12.txt (-32041, 34573) 2532
        0.95 real         0.19 user         0.02 sys

Compilation finished at Sat Dec 12 00:14:30

That's not the right answer; your answer is too low. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 2532.) [Return to Day 12]

-32041 34573 -32069 34524 :    []
part2 input.day12.txt (-32041 34573) (32041 34573) = MD 66614
        1.19 real         0.20 user         0.02 sys

Compilation finished at Sat Dec 12 00:20:15

*)

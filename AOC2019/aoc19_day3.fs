printfn "Advent of Code Day 3"
// Day 3
let a1 = System.IO.File.ReadAllLines("1")  |> Array.toList
let a2 = System.IO.File.ReadAllLines("2")   |> Array.toList
// printfn "%A" a1
// printfn "%A" a2



// let a1 = [ "R75" ; "D30" ; "R83" ; "U83" ; "L12" ; "D49" ; "R71" ; "U7" ; "L72" ]
// let a2 = [ "U62" ; "R66" ; "U55" ; "R34" ; "D71" ; "R55" ; "D58" ; "R83" ]

// let a1 = [ "R98" ; "U47" ; "R26" ; "D63" ; "R33" ; "U87" ; "L62" ; "D20" ; "R33" ; "U53" ; "R51" ]
// let a2 = [ "U98" ; "R91" ; "D20" ; "R16" ; "D67" ; "R40" ; "U7" ; "R15" ; "U6" ; "R7" ]


(*
let a1 = [ "R75" ; "D30" ; "R83" ; "U83" ; "L12" ; "D49" ; "R71" ; "U7" ; "L72" ]
let a2 = [ "U62" ; "R66" ; "U55" ; "R34" ; "D71" ; "R55" ; "D58" ; "R83" ]
// = distance 159

   R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159  PASS

R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135 PASS

let a1 = [ "R98" ; "U47" ; "R26" ; "D63" ; "R33" ; "U87" ; "L62" ; "D20" ; "R33" ; "U53" ; "R51" ]
let a2 = [ "U98" ; "R91" ; "D20" ; "R16" ; "D67" ; "R40" ; "U7" ; "R15" ; "U6" ; "R7" ]
           //  distance 135


   *)



let dxy (a,b) =
    match a with
        | 'U' -> (0,-b)
        | 'D' -> (0,b)
        | 'R' -> (b,0)
        | 'L' -> (-b,0)
        | _ -> printfn "ERROR: <<<<<<<<<<<<<<<< %c" a
               (0,0)


let rec aggr ( data : (int * int) list ) (cursor: int*int)  =
    if Seq.length data = 0 then []
    else
        let point = data.[0]
        let newcursor = (fst cursor + fst point, snd cursor + snd point)
        let tt =  data.[1..]
        newcursor :: ( aggr tt newcursor)

type Line =
 | HORZ of (int*int) * (int*int)
 | VERT of (int*int) * (int*int)
 
let sort_segment_ends  ((a1x,a1y),(b1x,b1y)) =
    if      a1x < b1x then   (a1x,a1y),(b1x,b1y)
    else if a1x > b1x then   (b1x,b1y),(a1x,a1y)
    else if a1y < b1y then   (a1x,a1y),(b1x,b1y)
    else                     (b1x,b1y),(a1x,a1y)

let input2segments (ina : string list )=
    let dir1 = ina |> List.map (fun c ->  c.[0],  System.Int32.Parse c.[1..] )    
    let dd = dir1 |> List.map dxy
    let pointlist = (0,0)::(aggr dd (0,0) )
    let numpoints = List.length pointlist
    List.zip pointlist.[0..(numpoints-2)] pointlist.[1..(numpoints-1)] |> List.map sort_segment_ends
    
let mhdist (x,y)  = abs(x) + abs(y)  // manhatten distance from origin

let s1 = (input2segments a1)
let s2 = (input2segments a2)

let input2segments_notsorted (ina : string list )=
    let dir1 = ina |> List.map (fun c ->  c.[0],  System.Int32.Parse c.[1..] )    
    let dd = dir1 |> List.map dxy
    let pointlist = (0,0)::(aggr dd (0,0) )
    let numpoints = List.length pointlist
    List.zip pointlist.[0..(numpoints-2)] pointlist.[1..(numpoints-1)] 

let s1ns = (input2segments_notsorted a1)
let s2ns = (input2segments_notsorted a2)

let points_at_which_pair_intersect ((a1x,a1y),(b1x,b1y)) ((a2x,a2y),(b2x,b2y)) =
    let horiz1 = (a1y=b1y)
    let horiz2 = (a2y=b2y)    
    if horiz1 && horiz2     // Both horizontral.
    then
        if not (a1y = a2y)
        then []
        else
            // cases
            // a1x -  b1x - a2x - b2x - none
            // a1x -  a2x - b1x - b2x - (max a1x a2x) - (min b1x b2x)
            // a1x -  a2x - b2x - b1x - (max a1x a2x) - (min b1x b2x)

            // a2x -  b2x - a1x - b1x - none
            // a2x -  a1x - b2x - b1x - (max a1x a2x) - (min b1x b2x)
            // a2x -  a1x - b1x - b2x - (max a1x a2x) - (min b1x b2x)

            if b1x < a2x || b2x < a1x 
                then []
                else
                    // intersects from (max a1x a2x) - (min b1x b2x) at a1y 
                    seq { for x in (max a1x a2x) .. (min b1x b2x) do yield  x, a1y } |> Seq.toList 
    else
        if not horiz1 && not horiz2 //  Both vertical.
        then
            if not (a1x = a2x)
            then []
            else
                if b1y < a2y || b2y < a1y
                    then []
                    else
                        // intersects from a2y to b1y at a1x
                        seq { for y in (max a1y a2y) .. (min b1y b2y) do yield  a1x, y} |> Seq.toList 
        else
            // perpendicular
            if horiz1
            then
                if a1x <= a2x && a2x <= b1x  && a2y <= a1y && a1y <= b2y then [ ( a2x, a1y ) ] 
                else []
            else // horiz2
                if a2x <= a1x && a1x <= b2x  && a1y <= a2y && a2y <= b1y then [ ( a1x, a2y ) ]
                else []

// printfn "%A"  s1
// printfn "%A"  s2
// printfn "%A"  s1.[0]
// printfn "%A"  s2.[0] 
// printfn "why not 0 ? %A" (points_at_which_pair_intersect  s1.[0] s2.[0])
let result = seq {
                    for k in s1 do
                       for j in s2 do
                                let p = ((points_at_which_pair_intersect  k j) |> List.map (fun c -> mhdist c, c)) |> List.sort
                                if p.Length > 0 then
                                    // printfn "\n\nk:%A\nj:%A\np:%A\n" p k j 
                                    yield p,k,j
                    }
printfn "%A\n" (result |> Seq.sort )
printfn "Answer part 1 (5319) is %A" (result |> Seq.toList |> List.sort ).[1]

// let rec convert_path_to_points path =
//     match path with
//         | h1::tail -> let ((a1x,a1y),(b1x,b1y)), ((a2x,a2y),(b2x,b2y)) = h1
//                       (seq { for x in (min a1x a2x)..(max b1x b2x) do
//                                 for y in (min a1y a2y)..(max b1y b2y) do
//                                     yield x,y
//                              } |> Seq.toList ) @ (convert_path_to_points tail)
//         | _ -> []                      

(* ========================================================================== *)
(* ========================================================================== *)

(* ========================================================================== *)
(* ========================================================================== *)
(*                      Part 2                                                *)

let segmentlen linesegment =
    let ((x1, y1), (x2, y2)) = linesegment
    mhdist ((x2-x1), (y2-y1))

let fraction linesegment (point :(int * int)) = 
    let ((x1, y1), (x2, y2)) = linesegment
    let xp, yp = point
    mhdist (xp-x1 , yp - y1)


let line_point_intersection linesegment  (point :(int * int)) =
    let ((x1, y1), (x2, y2)) = linesegment
    let xp, yp = point
    if x1 = x2  && xp = x1 // vertical line and we are on it
    then if y1 < y2
         then if yp >= y1 && yp <= y2 then true else false
         else if yp >= y2 && yp <= y1 then true else false
    else if y1=y2 && yp = y1 // else horizonal line && we are on it
         then if x1 < x2
              then if xp >= x1 && xp <= x2 then true else false
              else if xp >= x2 && xp <= x1 then true else false
         else false


// printfn ""

// printfn "line_point_intersection true %A " (line_point_intersection ((40,0), (1000,0)) ( 500,0))
// printfn "line_point_intersection test %A " (line_point_intersection ((40,0), (1000,0)) ( 500,1))
// printfn "line_point_intersection test %A " (line_point_intersection ((40,0), (1000,0)) ( 0,0))
// printfn "line_point_intersection test %A " (line_point_intersection ((40,0), (1000,0)) ( 1500,0))
                                                                          
// printfn "line_point_intersection true %A " (line_point_intersection ((0,40), (0,1000)) ( 0,500))
// printfn "line_point_intersection test %A " (line_point_intersection ((0,40), (0,1000)) ( 1,500))
// printfn "line_point_intersection test %A " (line_point_intersection ((0,40), (0,1000)) ( 0,0))
// printfn "line_point_intersection test %A " (line_point_intersection ((0,40), (0,1000)) ( 0,1500))
                                                                          
// printfn "line_point_intersection true %A " (line_point_intersection ((40,0), (-1000,0)) ( -500,0))
// printfn "line_point_intersection true %A " (line_point_intersection ((40,0), (-1000,0)) ( 0,0))
// printfn "line_point_intersection test %A " (line_point_intersection ((40,0), (-1000,0)) ( -500,1))
// printfn "line_point_intersection test %A " (line_point_intersection ((40,0), (-1000,0)) ( -1500,0))
                                                                          
// printfn "line_point_intersection true %A " (line_point_intersection ((0,40), (0,-1000)) ( 0,-500))
// printfn "line_point_intersection true %A " (line_point_intersection ((0,40), (0,-1000)) ( 0,0))
// printfn "line_point_intersection test %A " (line_point_intersection ((0,40), (0,-1000)) ( 1,-500))
// printfn "line_point_intersection test %A " (line_point_intersection ((0,40), (0,-1000)) ( 0,-1500))


// printfn "fraction %A " (fraction ((40,0),( 1000,0)) ( 500,0))
// printfn "fraction %A " (fraction ((0,40),( 0,1000)) ( 0,500))
// printfn "fraction %A " (fraction ((0,-40),( 0,-1000)) ( 0,-500))



let rec path_length_to path (apoint :(int * int)) dist =
    match path with
        | h1::tail -> if line_point_intersection h1 apoint
                      then
                          let f = fraction h1 apoint
                          dist + f
                      else path_length_to tail apoint (dist + (segmentlen h1))
        | []       -> 0                      

let combined_path_length_to path1 path2 point =
    (path_length_to path1 point 0) + (path_length_to path2 point 0) 


let point_of aresult = 
    let ([(_, point)], _, _ ) =   aresult
    point

let part2p = result |> Seq.map point_of 

printfn "part2p  %A" part2p

let part2pc = result |> Seq.map point_of |> Seq.map (combined_path_length_to s1ns s2ns) 

printfn "part2pc  %A" part2pc

let part2 = result |> Seq.map point_of |> Seq.map (combined_path_length_to s1ns s2ns) |> Seq.sort

printfn "part2  %A" part2

let ([(dist, point)], ls1, ls2 ) =     (Seq.item 0 result)
printfn "args of path_length_to %A "    (Seq.item 0 result)
printfn "args of path_length_to %A "    (Seq.item 1 result)
printfn "args %A %A %A %A" dist point ls1 ls2
printfn "point of %A" (point_of (Seq.item 0 result))
printfn ""
printfn "path_length_to %A" (path_length_to s1ns  point 0)
printfn "path_length_to %A" (path_length_to s2ns  point 0)
printfn "como length_to %A" (combined_path_length_to s1ns s2ns  point)
printfn ""
printfn "-------------------------------"
printfn ""


let rec convert_path_to_points path =
    match path with
        | h1::tail -> let ((a1x,a1y),(b1x,b1y)) = h1
                      (seq { for x in (min a1x b1x)..(max a1x b1x) do
                                for y in (min a1y b1y)..(max a1y b1y) do
                                    yield x,y
                             } |> Seq.toList ) @ (convert_path_to_points tail)
        | _ -> []                      

let s1_path = (convert_path_to_points s1)
let s2_path = (convert_path_to_points s2)

let steps_on_path_to_point path point =
    List.findIndex (fun c -> c=point) path

let combo_steps point =
    (steps_on_path_to_point s1_path point ) + (steps_on_path_to_point s2_path point )

printfn "s2_path: %A" s2_path
printfn "steps 1 %A" (steps_on_path_to_point s1_path (0,0))
// printfn "steps 1 %A" (steps_on_path_to_point s1_path (155,-4))
printfn "steps 2 %A" (steps_on_path_to_point s2_path (0,0))
// printfn "steps 2 %A" (steps_on_path_to_point s2_path (155,-4))
printfn "steps c %d" (combo_steps (0,0))
// printfn "steps c %d" (combo_steps (155,-4))

let sumdistlist = result |> Seq.map ( fun ([d, p], k, j) -> combo_steps p ) |> Seq.sort
printfn "sumdistlist: %A" sumdistlist
(*
   -*- mode: compilation; default-directory: "~/Dropbox/fsharp/aoc2019/" -*-
Compilation started at Sun Dec  8 17:41:23

make -k 
/Library/Frameworks/Mono.framework/Versions/Current/bin/fsharpc aoc19_day3.fs
Microsoft (R) F# Compiler version 4.1
Copyright (c) Microsoft Corporation. All Rights Reserved.
time /Library/Frameworks/Mono.framework/Versions/Current/bin/mono aoc19_day3.exe
Advent of Code Day 3


k:[(0, (0, 0))]
j:((0, 0), (995, 0))
p:((-999, 0), (0, 0))



k:[(5627, (562, 5065))]
j:((547, 5065), (905, 5065))
p:((562, 4726), (562, 5232))



k:[(5319, (562, 4757))]
j:((547, 4757), (1533, 4757))
p:((562, 4726), (562, 5232))



k:[(7447, (1421, 6026))]
j:((1421, 5319), (1421, 6177))
p:((974, 6026), (1749, 6026))



k:[(7329, (974, 6355))]
j:((499, 6355), (1486, 6355))
p:((974, 6026), (974, 6706))



k:[(7394, (499, 6895))]
j:((499, 6355), (499, 7017))
p:((50, 6895), (996, 6895))



k:[(7249, (499, 6750))]
j:((499, 6355), (499, 7017))
p:((223, 6750), (1179, 6750))



k:[(8013, (996, 7017))]
j:((499, 7017), (1270, 7017))
p:((996, 6895), (996, 7268))



k:[(8171, (1913, 6258))]
j:((1913, 6166), (1913, 7011))
p:((1741, 6258), (2471, 6258))



k:[(6321, (973, 5348))]
j:((973, 5179), (973, 6057))
p:((423, 5348), (1297, 5348))



k:[(6159, (973, 5186))]
j:((973, 5179), (973, 6057))
p:((457, 5186), (1297, 5186))



k:[(5707, (39, 5668))]
j:((39, 5252), (39, 6057))
p:((-455, 5668), (423, 5668))



k:[(5714, (-46, 5668))]
j:((-46, 5252), (-46, 6012))
p:((-455, 5668), (423, 5668))



k:[(6467, (-455, 6012))]
j:((-821, 6012), (-46, 6012))
p:((-455, 5668), (-455, 6610))



k:[(6506, (-494, 6012))]
j:((-821, 6012), (-46, 6012))
p:((-494, 5500), (-494, 6038))



k:[(6389, (-377, 6012))]
j:((-821, 6012), (-46, 6012))
p:((-377, 5825), (-377, 6038))



k:[(6536, (-524, 6012))]
j:((-821, 6012), (-46, 6012))
p:((-524, 5978), (-524, 6360))



k:[(7075, (-821, 6254))]
j:((-821, 6012), (-821, 6590))
p:((-919, 6254), (50, 6254))



k:[(7956, (-1366, 6590))]
j:((-1378, 6590), (-821, 6590))
p:((-1366, 6402), (-1366, 7312))



k:[(7685, (-1378, 6307))]
j:((-1378, 6046), (-1378, 6590))
p:((-2047, 6307), (-1139, 6307))



k:[(7780, (-1378, 6402))]
j:((-1378, 6046), (-1378, 6590))
p:((-2296, 6402), (-1366, 6402))



k:[(7938, (-1378, 6560))]
j:((-1378, 6046), (-1378, 6590))
p:((-1743, 6560), (-962, 6560))



k:[(7759, (-4099, 3660))]
j:((-4788, 3660), (-4083, 3660))
p:((-4099, 3480), (-4099, 3809))



k:[(7892, (-4083, 3809))]
j:((-4083, 3660), (-4083, 3958))
p:((-4099, 3809), (-3946, 3809))



k:[(7725, (-4114, 3611))]
j:((-4114, 3429), (-4114, 4394))
p:((-4221, 3611), (-3365, 3611))



k:[(7650, (-4221, 3429))]
j:((-4276, 3429), (-4114, 3429))
p:((-4221, 3222), (-4221, 3611))



k:[(6813, (-3365, 3448))]
j:((-4276, 3448), (-3326, 3448))
p:((-3365, 2642), (-3365, 3611))



k:[(7669, (-4221, 3448))]
j:((-4276, 3448), (-3326, 3448))
p:((-4221, 3222), (-4221, 3611))



k:[(7394, (-3946, 3448))]
j:((-4276, 3448), (-3326, 3448))
p:((-3946, 3222), (-3946, 3809))



k:[(6806, (-3326, 3480))]
j:((-3326, 3448), (-3326, 4030))
p:((-4099, 3480), (-3266, 3480))



k:[(6289, (-2183, 4106))]
j:((-2183, 3164), (-2183, 4127))
p:((-2367, 4106), (-1638, 4106))



k:[(5410, (-2246, 3164))]
j:((-2326, 3164), (-2183, 3164))
p:((-2246, 2472), (-2246, 3210))



k:[(5536, (-2326, 3210))]
j:((-2326, 3164), (-2326, 4101))
p:((-2367, 3210), (-2246, 3210))



k:[(6468, (-2367, 4101))]
j:((-3011, 4101), (-2326, 4101))
p:((-2367, 3210), (-2367, 4106))



k:[(7152, (-3749, 3403))]
j:((-3749, 3304), (-3749, 4263))
p:((-3961, 3403), (-3127, 3403))



k:[(7360, (-3749, 3611))]
j:((-3749, 3304), (-3749, 4263))
p:((-4221, 3611), (-3365, 3611))



k:[(7229, (-3749, 3480))]
j:((-3749, 3304), (-3749, 4263))
p:((-4099, 3480), (-3266, 3480))



k:[(6411, (-3852, 2559))]
j:((-3852, 2505), (-3852, 3304))
p:((-3961, 2559), (-3286, 2559))



k:[(6039, (-3480, 2559))]
j:((-3480, 2103), (-3480, 3024))
p:((-3961, 2559), (-3286, 2559))



k:[(6151, (-3127, 3024))]
j:((-3480, 3024), (-2565, 3024))
p:((-3127, 2738), (-3127, 3403))



k:[(6389, (-3365, 3024))]
j:((-3480, 3024), (-2565, 3024))
p:((-3365, 2642), (-3365, 3611))



k:[(6290, (-3266, 3024))]
j:((-3480, 3024), (-2565, 3024))
p:((-3266, 2718), (-3266, 3480))

Answer is ([(5319, (562, 4757))], ((547, 4757), (1533, 4757)), ((562, 4726), (562, 5232)))
        0.34 real         0.18 user         0.01 sys

Compilation finished at Sun Dec  8 17:41:27

5319 right answer first try
    
   *)


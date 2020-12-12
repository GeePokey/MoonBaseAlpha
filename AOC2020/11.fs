printfn "Advent of Code 2020 Day 11"
// Day 11


let lines1 = System.IO.File.ReadAllLines("input.day11.txt")

// let lines1 = System.IO.File.ReadAllLines("sample.day11.txt")
// let lines =  Array.map int lines1 

// let lines = lines1 |> Array.map (fun c -> c.ToCharArray() )

let width  = lines1.[0] |> Seq.length
let height = lines1     |> Seq.length

let lines = Array2D.init height width (fun y x -> lines1.[y].[x] ) //.Chars.[x] )

// printfn "%A" lines

printfn "W %d H %d" width height
    
[<Literal>]
let FLOOR = '.'

[<Literal>]
let OCCUPIED = '#'

[<Literal>]
let CHAIR = 'L'


let neighbooroffsets = seq { for x in [-1..1] do
                                for y in [-1..1] do
                                   if not (x = 0 && y = 0) then
                                    yield (x, y)
                         }

let tmpa = neighbooroffsets |> Seq.toArray
printfn "neighbooroffsets = %A  %A  %A" tmpa.[0] tmpa.[1] tmpa.[2]
printfn "neighbooroffsets = %A            %A" tmpa.[3] tmpa.[4]
printfn "neighbooroffsets = %A  %A    %A" tmpa.[5] tmpa.[6] tmpa.[7]

let read_cell ( data : char [,]) x y =
    // printfn "%d %d %A" x y data.[y,x]
    if x < 0 ||  x >= width then FLOOR
    else if y < 0  || y>= height then  FLOOR
        else
            data.[y,x]
            

let neighboors data x y =
    neighbooroffsets |> Seq.sumBy (fun (dx,dy) -> if (read_cell data ( x + dx )  ( y + dy )) = OCCUPIED then 1 else 0 )


// Part 2
let read_cell_radially ( data : char [,] ) ax ay dx dy =
    let mutable x = ax + dx
    let mutable y = ay + dy
//    while x > 1 && y > 1 && x < (width-1) && y < (height-1) && data.[y,x] =  FLOOR do
    while x >= 0 && y >= 0 && x < width && y < height && data.[y,x] = FLOOR do
        x <- x + dx
        y <- y + dy
    if x >= 0 && y >= 0 && x < width && y < height then data.[y,x] else FLOOR


// Part 2        
let neighboors_part2 data x y =
    neighbooroffsets |> Seq.sumBy (fun (dx,dy) -> if (read_cell_radially data  x  y dx dy) = OCCUPIED then 1 else 0 )


let dump ( (grid: char [,] ) , modflag, counti ) =
    printfn "Mod: %A count %d" modflag counti
    for row in [0..height-1] do
        for col in [0..width-1] do 
           printf "%c" grid.[row,col] 
        printfn ""

(*
 If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
 
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.

Otherwise, the seat's state does not change.
             *)
             
let updatex neighboorpartx ocx (data : char [,]  ) :  char [,] * bool * int =
    let mutable dest = Array2D.create  height width FLOOR
    // dump dest
    let mutable modified = false
    let mutable modcount = 0


    for y in [0.. height - 1 ] do
        for x in [0.. width - 1 ] do
            match (read_cell data x y ), (neighboorpartx data x y) with
                | FLOOR, _    -> ()  // dest.[y,x] <- FLOOR
                | OCCUPIED, oc when oc >= ocx -> dest.[y,x] <- CHAIR
                                                 modified <- true
                                                 modcount <- modcount + 1
                                                 // printfn "E: %d,%d" x y 
                | CHAIR, 0    -> dest.[y,x] <- OCCUPIED
                                 modified <- true
                                 modcount <- modcount + 1                                 
                                 // printfn "O: %d,%d" x y
                | state,cc     -> dest.[y,x] <- state
                                  // printfn "S: %d,%d = %d" x y cc
    dest, modified , modcount


// let  update = updatex neighboors 4
let  update = updatex neighboors_part2 5

let third (_, _, c) = c
let my2 (_, c, _ ) = c
let my1 (c, _, _) = c


printfn "Main"
dump (lines, false, 0)
let mutable x =  lines, true, 0
let mutable passes = 0
while (my2 x) do
    passes <- passes + 1
    x <- update (my1 x)
    printfn "\npass %5d %4d %A\n" passes (third x) (my2 x)
    // dump x

let countdump test (grid: char [,] ) =
    seq {
        for row in [0..height-1] do
          for col in [0..width-1] do
            if (test grid.[row,col])
            then yield 1
}

dump x
printfn "Part 2 passes %d count occupied %d " passes ((my1 x) |> countdump (fun c ->  c = OCCUPIED) |> Seq.length )


(*   
1st attempt (test data DUH)
##.#L#.###
Part 1 passes 5 count occupied 50
        0.14 real         0.12 user         0.01 sys

Compilation finished at Thu Dec 10 23:24:09


2nd attempt (still test data DUH)
##.#L#.###
Part 1 passes 5 count occupied 45 
        0.14 real         0.12 user         0.01 sys

Compilation finished at Thu Dec 10 23:24:09

And not correct for test data either!!  incoming data was rotated jesus take the wheel!!


Got the right answer for sample!
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
Part 1 passes 6 count occupied 37 
        0.34 real         0.14 user         0.01 sys

Compilation finished at Thu Dec 10 23:51:28

Part 1 passes 95 count occupied 2424 
        1.69 real         1.05 user         0.04 sys

Compilation finished at Thu Dec 10 23:57:00

*)

(*
 part 2
That's not the right answer; your answer is too high. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 2330.) [Return to Day 11]


Part 1 passes 88 count occupied 2330 
        2.28 real         1.17 user         0.05 sys

Compilation finished at Fri Dec 11 22:13:07



#.LLLLL#.L
#.L#LL#.L#
Part 2 passes 7 count occupied 26  // correct answer for sample part 2!
        0.18 real         0.14 user         0.01 sys

Compilation finished at Fri Dec 11 22:25:27


L#L#L#L.#L#L#
Part 2 passes 89 count occupied 2208 
        2.14 real         1.21 user         0.05 sys

Compilation finished at Fri Dec 11 22:26:56
*)

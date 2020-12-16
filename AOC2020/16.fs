printfn "Advent of Code 2020 Day 16"



// let filespec = "sample.day16.txt"
// let filespec = "sample2.day12.txt"
let filespec = "input.day16.txt"
let lines = System.IO.File.ReadAllLines(filespec) |> Array.toList
// let lines =  Array.map int lines1 

// let lines = lines1 |> Array.map (fun c -> c.ToCharArray() )


// printfn "%A" lines

open System
open System.IO
open System.Text.RegularExpressions


let splitBy (c : string) f (str : string) = str.Split([| c |], StringSplitOptions.None) |> f
    

let (|Regex|_|) pattern input =
    let m = Regex.Match(input, pattern)
    if m.Success then Some(List.tail [ for g in m.Groups -> g.Value ])
    else None

let validate_ticket (rules : (int*int*int*int) list) (fs:int []) =
    
     let sub  a (r1, r2, r3, r4) = (r1 <= a && a <= r2) || (r3 <= a && a <= r4) 

     //     let sub2 a b c (r1, r2, r3, r4) = (sub a r1 r2 r3 r4 ) + (sub b r1 r2 r3 r4 ) + (sub c r1 r2 r3 r4 )

     let goodvalue q = rules |> List.exists (sub q)
     let badvalue q = not (goodvalue q)

     let z = fs |> Array.sumBy (fun a -> if badvalue a then a else 0 )
     printfn "%d <= %A   " z fs
     z

let dump_rules rules = for i in rules do
                         printfn "%A" i

let rec handle_input codes rules (accum : int ) =
    match codes with
        | h::tail -> match h with
                       | Regex @".*: (\d+)-(\d+) or (\d+)-(\d+)" [a;b;c;d] -> handle_input tail ((int a, int b, int c, int d)::rules)  accum
                       | "" -> handle_input tail rules accum
                       | "your ticket:" -> handle_input tail rules accum
                       | "nearby tickets:" -> dump_rules rules
                                              handle_input tail rules accum
                       | Regex @"([0-9,]+)"  [str]         ->  let fields = (h.Split( [|","|], StringSplitOptions.None )) |> Array.map int
                                                               let subaccum = validate_ticket rules fields
                                                               handle_input tail rules (accum + subaccum)
                       | _ -> handle_input tail rules accum
                       
        | _ -> accum


printfn "handle_input %A (22000)" ( handle_input lines [] 0 )

(*

part1 440; 788; 662; 555; 834; 527; 434;
  853; 854; 374; 555|]   
handle_input 22000 
        2.18 real         0.52 user         0.02 sys

Compilation finished at Tue Dec 15 22:27:09

*)

// Name: Wade Moulton
// Date: 12/04/2020
// Course: CS 4306 Section 04
// Assignment: Final Project


//initialize graph representation
const graph = {
    A: {B:3, C:4, D:6},
    B: {A:3, C:5, E:11},
    C: {A:4, B:5, D:7, F:5},
    D: {A:6, C:7, F:4},
    E: {B:11, F:8},
    F: {C:5, D:4, E:8}
};

//initialize variables
let update_paths = {};
let visited = [];
let unvisited = [];
let init_dist = 0;

//function to find given value index and then remove from array
function RemoveVertexFromUnvisited(curr_vertex) {
    for(let i = 0; i < unvisited.length; i++){
        if(unvisited[i] === curr_vertex) {
            unvisited.splice(i, 1);
        }
    }
}

function DijkstraAlgorithm(graph, start, end) {
    //clear all variables at beginning of function
    update_paths = {};
    visited = [];
    unvisited = [];
    init_dist = 0;

    //push all vertices to the unvisited array
    for(let vertex in graph) {
        unvisited.push(vertex);
    }

    //assign initial values in update_paths for each vertex
    for(let vertex in graph){
        update_paths[vertex] = {distance_from_a: Infinity, prev_vertex: null};
    }
    //make sure distance from start for the start vertex is 0
    update_paths[start].distance_from_a = 0;

    //initialize current vertex to the supplied starting vertex
    let curr_vertex = start;
    //loop should iterate until all vertices have been visited
    while(unvisited.length > 0) {
        //iterate through every connected node to the current vertex
        //check whether the value of the weight plus the current distance < current distance from a
        //if it is less update the distance from a for current node and assign the previous vertex
        for(let node in graph[curr_vertex]) {
            if(graph[curr_vertex][node] + init_dist < update_paths[node].distance_from_a) {
                update_paths[node].distance_from_a = graph[curr_vertex][node] + init_dist;
                update_paths[node].prev_vertex = curr_vertex;
            }
        }
        //mark current vertex as visited
        visited.push(curr_vertex);
        //remove the curernt vertex from the unvisited array
        RemoveVertexFromUnvisited(curr_vertex);
        //initialize variables for comparison of which node should be visited next
        let curr_min_vertex = '';
        let curr_min_value = Infinity;

        //iterate though remaining unvisited nodes
        unvisited.forEach(vertex => {
            //if the distance from a is less than current min value update current min value
            //also update the initial distance to the current min value
            //assign the next lowest weight vertex that should be visited
            if(update_paths[vertex].distance_from_a < curr_min_value) {
                curr_min_value = update_paths[vertex].distance_from_a;
                init_dist = curr_min_value;
                curr_min_vertex = vertex;
            }
        })
        //assign the next vertex that should be visited
        curr_vertex = curr_min_vertex;
    }
    //create array to track the path taken for the minimum distance from start to end vertices
    let best_path_arr = [];
    let final = end;
    //iterate backwards from end vertex to start and assign the previous visited vertices to array
    while(final !== start) {
        best_path_arr.unshift(final);
        final = update_paths[final].prev_vertex;
    }
    //add the start node to the paths array
    best_path_arr.unshift(start);
    //create string from paths array to create visualization of taken path
    let best_path_str = '';
    best_path_arr.forEach(element => {
        if(element === start) {
            best_path_str += element;
        }
        else {
            best_path_str += ` -> ${element}`;
        }
    })
    //return the total distance of shortest path as well as the path string
    return [update_paths[end].distance_from_a, best_path_str];
}

//assign result of function call to variable
const result = DijkstraAlgorithm(graph, "A", "F");
//print results of function call to console in a formatted string
console.log(`Dijkstra's Algorithm\nShortest Distance: ${result[0]}\nShortest Path: ${result[1]}`);

//initialize array to store all weights
let edge_weights = [];
//assign values for each vertex in graph to edge weights array
for(let vertex in graph) {
    for(let node in graph[vertex]) {
        //include both ends of current connection and the weight of that connection
        //will assign for both directions since the graph is undirected
        edge_weights.push({v1: vertex, v2: node, weight: graph[vertex][node]});
    }
}

function BubbleSort(arr) {
    //iterate through array using nested loop
    for(let i = 0; i < arr.length - 1; i++) {
        for(let j = 0; j < arr.length - 1 - i; j++) {
            //if next value is less than current value swap the position of the two values
            if(arr[j + 1].weight < arr[j].weight) {
                let tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }
    }
    //return the sorted array
    return arr;
}

console.log(`All ${edge_weights.length} connections sorted by weight using Bubble Sort:\n`);
console.log(BubbleSort(edge_weights));
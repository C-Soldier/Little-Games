#include <iostream>
#include <string>
#include <unordered_map>
#include <random>
#include <limits>
#include <ranges>

using namespace std;

// Function to roll a six-sided die
int die_roll(){
    random_device rd;

    mt19937 gen(rd());

    uniform_int_distribution<> distrib(1, 6);

    return distrib(gen);
};

// Function to check the square condition for snakes and ladders or if the player has won or rolled too high
void square_condition(string player, int &player_postion, int die_num, bool &game_status){
    unordered_map<int, int> const snakes = {
        {17, 7},
        {54, 34},
        {62, 19},
        {64, 60},
        {87, 24},
        {93, 73},
        {95, 75},
        {99, 78},

    };

    unordered_map<int, int> const ladders = {
        {4, 14},
        {9, 31},
        {20, 38},
        {28, 84},
        {40, 59},
        {51, 67},
        {63, 81},
        {71, 91},
    };

    
    if(player_postion == 100){
        cout << player << " WINS!!!" << endl;
        game_status = false;
    }
    else if(player_postion > 100){
        player_postion -= die_num;
        cout << player << " rolled too high" << "\n" << "Roll an exact number to win" << endl;
    }    
    else if(player_postion < 100){
        for(const auto& pair : snakes){
            if(player_postion == pair.first){
                player_postion = pair.second;
                cout << player << " landed on a snake\n" << player << " is now on " << player_postion << endl;
                break;
            };
        };
        
        for(const auto& pair : ladders){
            if(player_postion == pair.first){
                player_postion = pair.second;
                cout << player << " landed on a ladder\n" << player << " is now on " << player_postion << endl;
                break;
            };
        };
    };
};

int main(){
   
    int num_of_players;
    string player_name;
    bool game_running = true;
    unordered_map<string, int> idle_players;
    unordered_map<string, int> players;

    cout << "How many players?: ";
    cin >> num_of_players;

    for(int num = 1; num != num_of_players + 1; num++){
        cout << "Enter the name of player " << num << ": ";
        cin >> player_name;

        idle_players.insert(make_pair(player_name, 0));

    };
    // Game loop
    while(game_running){
        // Idle players loop
        if(not idle_players.empty()){        
            for (auto& pair : idle_players){
                for(const auto& pair : idle_players){
                    cout << pair.first << ":" << pair.second << "\n" << endl;
                };

                cout << pair.first << " turn" << "\n" << "Click ENTER to roll die... ";   
                cin.ignore(numeric_limits<streamsize>::max(), '\n');  
                cin.get();
                int die_num = die_roll();
                
                if(die_num != 6){
                    cout << pair.first << " rolled a " << die_num << "\n" << pair.first << " can't move" << endl;
                }
                else{
                    cout << pair.first << " rolled a " << die_num << "\n" << pair.first << " can move" << endl; 

                    cout << pair.first << " turn" << "\n" << "Click ENTER to roll die... ";    
                    cin.ignore(numeric_limits<streamsize>::max(), '\n'); 
                    cin.get();
                    int die_num = die_roll();

                    pair.second += die_num;
                    cout << pair.first << " rolled a " << die_num << "\n" << pair.first << " is now on " << pair.second << endl;

                    // What happens if the player rolls a 6
                    while(die_num == 6){
                        cout << pair.first << " turn" << "\n" << "Click ENTER to roll die again... ";  
                        cin.ignore(numeric_limits<streamsize>::max(), '\n');
                        cin.get();
                        int die_num = die_roll();  

                        pair.second += die_num;
                        cout << pair.first << " rolled a " << die_num << "\n" << pair.first << " is now on " << pair.second << endl;                   

                        square_condition(pair.first, pair.second, die_num, game_running);
                        if(game_running == false){
                            break;
                        };

                        if(die_num != 6){
                            break;
                        };
                    };

                    players.insert({pair.first, pair.second});
                    idle_players.erase(pair.first);
                };
            };
        
        };

        // Active players loop
        if(not players.empty() and game_running == true){
            for (auto& pair : players){
                for(const auto& pair : players){
                    cout << pair.first << ":" << pair.second << "\n" << endl;
                };

                cout << pair.first << " turn" << "\n" << "Click ENTER to roll die... ";   
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                cin.get();
                int die_num = die_roll();

                pair.second += die_num;
                cout << pair.first << " rolled a " << die_num << "\n" << pair.first << " is now on " << pair.second << endl;

                // What happens if the player rolls a 6
                while(die_num == 6){
                    cout << pair.first << " turn" << "\n" << "Click ENTER to roll die again... ";  
                    cin.ignore(numeric_limits<streamsize>::max(), '\n');
                    cin.get();
                    int die_num = die_roll();  

                    pair.second += die_num;
                    cout << pair.first << " rolled a " << die_num << "\n" << pair.first << " is now on " << pair.second << endl;                   

                    square_condition(pair.first, pair.second, die_num, game_running);
                    if(game_running == false){
                        break;
                    };

                    if(die_num != 6){
                        break;
                    };

                };

                square_condition(pair.first, pair.second, die_num, game_running);
                if(game_running == false){
                        break;
                    };


            };

        };
    
    };


    return 0;
}
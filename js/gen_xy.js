function gen_x(i,d){
                    var x;
                    if(i<3){
                        switch (i) {
                            case 0:
                                x = -d;
                                break;
                            case 1:
                                x = 0;
                                break;
                            case 2:
                                x = d;
                                break;
                        }
                    }else if(i<6){
                        switch (i) {
                            case 3:
                                x = -d;
                                break;
                            case 4:
                                x = 0;
                                break;
                            case 5:
                                x = d;
                                break;
                        }
                    }else{
                        switch (i) {
                            case 6:
                                x = -d;
                                break;
                            case 7:
                                x = 0;
                                break;
                            case 8:
                                x = d;
                                break;
                        }
                    }
                    return x;
                }
                function gen_y(i,d){
                    var x;
                    if(i<3){
                        x = -d;
                    }else if(i<6){
                        x = 0;
                    }else{
                        x = d;
                    }
                    return x;
                }
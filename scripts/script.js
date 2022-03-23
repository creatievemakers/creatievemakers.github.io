
    // setup the first .html File
    // function startup() {
    
    //     fetch("site/startup.html")
    //     .then(res=>res.text())
    //     .then((txt) => {
    //         document.getElementById("container").innerHTML = txt;
            
    //     })
    //     }
        

// select the correct .html file

function aload (clicked_id) {

fetch("site/"+clicked_id+".html")
.then(res=>res.text())
.then((txt) => {
    document.getElementById("container").innerHTML = txt;
    document.title = "cm³ — "+ clicked_id;
    // window.location.href = "http://localhost:10001/?page=" + clicked_id

    console.log(clicked_id);
})
}

// -----------------------------------------------------------

    // logo functionality (wip)

    let images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','12.jpg','13.jpg','14.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','12.jpg','13.jpg','14.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','12.jpg','13.jpg','14.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','12.jpg','13.jpg','14.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','12.jpg','13.jpg','14.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','12.jpg','13.jpg','14.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','12.jpg','13.jpg','14.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','12.jpg','13.jpg','14.jpg','1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg','11.jpg','12.jpg','12.jpg','13.jpg','14.jpg'];

    const delayTime = 20
    let length = Math.min(images.length , 20)
    
    function add_function(){
            adding(0);
    }
    function sub_function(){
        sub(length);
    }
    
    let array = []
    function adding(i) {
    if (i < length)
        setTimeout(function() {
            adding(i + 1)

            array.push("<img src = \"../media/content/logo/"  + images[Math.floor(Math.random()*length)] + "\">")
            
            document.getElementById("f").innerHTML = array.join(",")






                // anti-glitch
                if(Object.keys(array).length > length){
                    array = []
                    console.log("doe da ne keer ni");
                }
            }, delayTime);
    }
    

    function sub(i) {
        if (i >= 0)
            setTimeout(function() {
                sub(i - 1)
                array.shift(i)
                // array.pop(i)
                document.getElementById("f").innerHTML = array.join()
                // console.log(array);
                }, delayTime);
        }





        // -----------------------------------------------------------
    
        // animation on index.html
    
        var inter = ['inter','multi','trans'];
        var courses = ['courses', 'electives', 'projects', 'summerschools', 'workshops']
        var disciplines = ['architects', 'engineers','artists']
        var years = ['5', '10','1','100','2','3','7','5','1','3','9','4','6','8']
        
        function a_inter() {
            
            document.getElementById('a_projects').innerHTML = courses[Math.floor(Math.random()*courses.length)];
            document.getElementById('a_inter').innerHTML = inter[Math.floor(Math.random()*inter.length)];
            
            setTimeout(a_inter, 500);    
        };
        a_inter();

        function b_inter() {
            
            document.getElementById('a_dis').innerHTML = disciplines[Math.floor(Math.random()*disciplines.length)];
            document.getElementById('a_years').innerHTML = years[Math.floor(Math.random()*years.length)];
            setTimeout(b_inter, 200);    
        };
        b_inter();


        // -----------------------------------------------------------


        // git functionality
        function requestUserRepos(username){
    
            const xhr = new XMLHttpRequest();
            const url = `https://api.github.com/orgs/${username}/repos`;
            
            // https://api.github.com/repos/creatievemakers/creatievemakers.github.io/commits ==> get the date of the commit
               https://api.github.com/repos/creatievemakers/creatievemakers.github.io/commits
            
            xhr.open('GET', url, true);
            
            // When request is received process it here
            xhr.onload = function() {

                
                const data = JSON.parse(this.response);
                
                const foo = url.replace("/repos" , "/creatievemakers.github.io/commits").replace("orgs", "repos")
                xhr.open('GET', foo, true);
                xhr.onload = function() {
                    const bar = JSON.parse(this.response);
                    const data = bar[0].commit.author.date
                     


                    let date = data.split("T")[0]                
                    const date_year =data.split("-")[0]
                    const date_month =data.split("-")[1]
                    const date_day =date.split("-")[2]
                    date = date_day + "-" + date_month+ "-" + date_year

                    let time = data.split("T")[1]
                    const time_hour= parseInt(time.split(":")[0])+1
                    
                    const time_min= time.split(":")[1]
                    time =  time_hour + ":" + time_min + "h"

                    const date_time = date  + " @ " +time
                    document.getElementById("latest-update").innerHTML ="latest update: " + date_time + "<span id=\"date_time_branch\"></span> "

                    document.getElementById("date_time_branch").innerHTML =" on branch " + "["
                     + "<a href=\"https://github.com/creatievemakers/creatievemakers.github.io\" id=\"links\" \">main</a>" + "]"
                }
                xhr.send();
                

                // run over all repositories and display them in menu
                for (let i in data) {
                    
                    const repo = data[i].name
                    const newP = document.createElement(`span`)
                    const newA = document.createElement(`a`)
                    newA.setAttribute("href",`https://github.com/${username}/${repo}`);
                    newA.setAttribute("target","_blank");
                    
                    const newDiv = document.createElement('div')
                    newDiv.setAttribute("id", "git_links")
                    const bar = document.createElement('span')  
                    newDiv.setAttribute("class","anim");
                    const name = document.createTextNode(data[i].name)
                    // const update = document.createTextNode(data[i].updated_at)
                    // add the text node to the newly created div
                    newA.appendChild(name)
                    // newP.appendChild(update)
                    newDiv.appendChild(newA)
                    newDiv.appendChild(newP)
                    const git = document.getElementById("git")
                    git.appendChild(newDiv)

                }
            }
            xhr.send();
        }
        
        requestUserRepos('creatievemakers');


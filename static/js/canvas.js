const canvas = document.getElementById("bgCanvas");

const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let particles = [];

class Particle{

    constructor(){

        this.x=Math.random()*canvas.width;
        this.y=Math.random()*canvas.height;

        this.radius=Math.random()*3+1;

        this.dx=(Math.random()-0.5)*0.8;
        this.dy=(Math.random()-0.5)*0.8;
    }

    draw(){

        ctx.beginPath();

        ctx.arc(this.x,this.y,this.radius,0,Math.PI*2);

        ctx.fillStyle="rgba(255,255,255,.7)";

        ctx.fill();

    }

    update(){

        this.x+=this.dx;
        this.y+=this.dy;

        if(this.x<0||this.x>canvas.width)
            this.dx*=-1;

        if(this.y<0||this.y>canvas.height)
            this.dy*=-1;

        this.draw();

    }

}

for(let i=0;i<120;i++){

    particles.push(new Particle());

}

function animate(){

    ctx.fillStyle="#081126";

    ctx.fillRect(0,0,canvas.width,canvas.height);

    particles.forEach(p=>p.update());

    requestAnimationFrame(animate);

}

animate();

window.addEventListener("resize",()=>{

    canvas.width=window.innerWidth;

    canvas.height=window.innerHeight;

});
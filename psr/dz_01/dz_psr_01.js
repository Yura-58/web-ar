import * as THREE from 'three';
import { MindARThree } from 'mindar-image-three';

document.addEventListener("DOMContentLoaded", () => {
const start = async() => {
const mindarThree = new MindARThree({
container: document.body,
imageTargetSrc: "../../assets/ploshaVM.mind",
});
const {renderer, scene, camera} = mindarThree;
const anchor = mindarThree.addAnchor(0);

const geometry = new THREE.PlaneGeometry(1, 1);
const material = new THREE.MeshBasicMaterial({
color: 0x00ffff, transparent: true, opacity: 0.5
});
const plane = new THREE.Mesh(geometry, material);
anchor.group.add(plane);

const geometry2 = new THREE.BoxGeometry( 1, 1, 1 );
const box = new THREE.Mesh(geometry2, material);
anchor.group.add(box);

const geometry3 = new THREE.SphereGeometry( 0.5, 32, 16 );
const sphere= new THREE.Mesh(geometry3, material);
anchor.group.add(sphere);

plane.position.x = 1;
box.position.x = -1;
sphere.position.x = 0;
sphere.position.y = 1.5;

await mindarThree.start();
renderer.setAnimationLoop(() => {
renderer.render(scene, camera);
});

}
start();


});
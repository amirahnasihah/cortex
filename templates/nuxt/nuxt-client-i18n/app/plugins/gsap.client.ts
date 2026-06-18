/**
 * GSAP — optional. Only loaded when animation is needed.
 * Keep animation isolated from layout logic.
 */
export default defineNuxtPlugin(() => {
  // When gsap is added: import gsap from 'gsap', import ScrollTrigger from 'gsap/ScrollTrigger', register and provide
  return {
    provide: {
      gsap: null,
      ScrollTrigger: null,
    },
  }
})

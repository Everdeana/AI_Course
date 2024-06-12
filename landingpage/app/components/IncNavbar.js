
"use client"

import { useState } from "react";
import { FiMenu } from "react-icons/fi";
import { FiX } from "react-icons/fi";


export default function IncNavbar() {

	const [nav, setNav] = useState(false);

	const handleNav = () => {
		setNav(!nav)
	}


	return (
		<div className="NAV">
			<div className="flex justify-between items-center h-24 max-w-[1240px] mx-auto px-4 text-white">
				<h1 className="w-full text-3xl font-bold text-[#354B46] m-4">MedEase</h1>
				<ul className="hidden md:flex">
					<li className="p-4">Home</li>
					<li className="p-4">Company</li>
					<li className="p-4">Product</li>
					<li className="p-4">About</li>
					<li className="p-4">Contact</li>
				</ul>
				<div className="block md:hidden" onClick={handleNav}>
					{!nav ? <FiX size={30} /> : <FiMenu size={40} />}
				</div>
				<div className={!nav ? "md:hidden fixed left-0 top-[90px] w-[50%] h-full border-r border-r-gray-900 bg-[#97B1AA] ease-in-out duration-500" : "md:hidden fixed left-[100%]"}>
					<ul className="p-4 uppercase">
						<li className="p-4 border-b border-gray-600">Home</li>
						<li className="p-4 border-b border-gray-600">Company</li>
						<li className="p-4 border-b border-gray-600">Product</li>
						<li className="p-4 border-b border-gray-600">About</li>
						<li className="p-4 border-b border-gray-600">Contact</li>
					</ul>
				</div>
			</div>
		</div>

	)
}

